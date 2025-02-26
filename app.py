import streamlit as st
import pandas as pd
from utils import fetch_crypto_info, plot_price_history
from coin_oracle import get_llama_response 

# Streamlit app title
st.title("CoinPulse: Real-Time Crypto Insights")

# Cryptocurrency input as a multi-select dropdown
crypto_options = ['bitcoin', 'ethereum', 'dogecoin', 'litecoin', 'ripple', 'cardano']
selected_cryptos = st.multiselect("Select cryptocurrencies:", crypto_options, default=["bitcoin", "ethereum"])

# Slider for selecting historical data range
days = st.slider("Select the number of days for price history:", min_value=1, max_value=365, value=7)

# Display cryptocurrency information
if st.button("Get Cryptocurrency Info"):
    with st.spinner("Fetching cryptocurrency info..."):
        crypto_info_list = fetch_crypto_info(selected_cryptos)

    if isinstance(crypto_info_list, list):
        st.subheader("Cryptocurrency Comparison:")
        comparison_df = pd.DataFrame(crypto_info_list)

        # Format prices and percentages
        comparison_df['current_price'] = comparison_df['current_price'].apply(lambda x: f"${x:,.2f}")
        comparison_df['price_change_percentage_24h'] = comparison_df['price_change_percentage_24h'].apply(
            lambda x: f"{x:.2f}%" if x > 0 else f"{x:.2f}%"
        )

        # Apply color formatting for price change
        def color_price_change(val):
            color = 'green' if float(val[:-1]) > 0 else 'red'
            return f'color: {color}'

        styled_df = comparison_df.style.applymap(color_price_change, subset=['price_change_percentage_24h'])
        st.dataframe(styled_df)

        # Plot the price history for all selected cryptocurrencies
        plot_price_history(selected_cryptos, days)

        # Get AI-based insights for each cryptocurrency
        for crypto in selected_cryptos:
            if st.button(f"Get Insights for {crypto.capitalize()} from LLaMA"):
                with st.spinner(f"Fetching insights for {crypto.capitalize()}..."):
                    insights_response = get_llama_response(f"Tell me about {crypto}.")
                st.subheader(f"Insights for {crypto.capitalize()} from LLaMA:")
                if "Error" in insights_response:
                    st.error(insights_response)
                else:
                    st.write(insights_response)
    else:
        st.error(crypto_info_list.get("error", "Could not retrieve cryptocurrency information."))
