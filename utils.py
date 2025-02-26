import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from together import Together
import os
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)

# Caching API requests to avoid repeated calls
@st.cache_data(ttl=600)
def fetch_crypto_info(cryptos):
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={','.join(cryptos)}&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        crypto_info_list = []
        for coin_data in data:
            crypto_info_list.append({
                "name": coin_data["name"],
                "current_price": coin_data["current_price"],
                "price_change_percentage_24h": coin_data["price_change_percentage_24h"],
                "market_cap": coin_data["market_cap"],
                "total_volume": coin_data["total_volume"],
                "circulating_supply": coin_data["circulating_supply"],
            })
        return crypto_info_list
    except Exception as e:
        return {"error": str(e)}

def plot_price_history(cryptos, days):
    """
    Fetches and plots the historical price data for the specified cryptocurrencies over the selected number of days.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    for crypto in cryptos:
        url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days={days}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            prices = data['prices']
            df = pd.DataFrame(prices, columns=['timestamp', 'price'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

            ax.plot(df['timestamp'], df['price'], label=f'{crypto.capitalize()} Price')
        except Exception as e:
            st.error(f"Error fetching price history for {crypto}: {str(e)}")

    ax.set_title(f'Cryptocurrency Price History (Last {days} Days)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price in USD')
    ax.tick_params(axis='x', rotation=45)
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)

def get_llama_response(crypto):
    """
    Sends a prompt to the Together AI LLaMA model and retrieves insights about the cryptocurrency.
    """
    try:
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
            messages=[{"role": "user", "content": f"Tell me about {crypto}."}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error retrieving response: {str(e)}"
