Coin Oracle: Cryptocurrency Insights Application
Coin Oracle is a user-friendly application that provides real-time data and AI-generated insights on cryptocurrencies. Built with Streamlit, it allows users to explore current prices, market trends, and historical data, while leveraging the LLaMA model via Together API for in-depth insights.

Features
Real-Time Data: Fetch current prices, market cap, and volume for selected cryptocurrencies.
Historical Trends: Visualize price trends over customizable periods.
AI Insights: Generate cryptocurrency insights using the LLaMA model.
Interactive UI: Built with Streamlit for ease of use.
Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/<your-username>/Coin_Oracle.git
cd Coin_Oracle
Create a Virtual Environment:

bash
Copy
Edit
python -m venv env
env\Scripts\activate  # Windows
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set Up API Key: Create a .env file and add your Together API key:

plaintext
Copy
Edit
TOGETHER_API_KEY=<your_api_key>
Run the App:

bash
Copy
Edit
streamlit run app.py
File Structure
plaintext
Copy
Edit
Coin_Oracle/
├── app.py          # Main application
├── crypto_agent.py  # AI insights with Together API
├── utils.py        # Helper functions for data fetching and plotting
├── config.py       # Environment configuration
├── requirements.txt # Dependencies
└── README.md       # Project documentation
Technologies
Streamlit: For building the app interface.
Pandas, Matplotlib: For data manipulation and visualization.
Together API: For AI insights with LLaMA model.
Requests: For API data fetching.
License
This project is licensed under the MIT License.
