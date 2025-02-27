# **Coin Oracle: Cryptocurrency Insights Application**  

**Coin Oracle** is a user-friendly application that provides **real-time data** and **AI-generated insights** on cryptocurrencies. Built with **Streamlit**, it allows users to explore current prices, market trends, and historical data while leveraging the **LLaMA model** via **Together API** for in-depth insights.  

---

## **🚀 Features**  

- **Real-Time Data** – Fetch current prices, market cap, and volume for selected cryptocurrencies.  
- **Historical Trends** – Visualize price trends over customizable periods.  
- **AI Insights** – Generate cryptocurrency insights using the **LLaMA model**.  
- **Interactive UI** – Built with **Streamlit** for ease of use.  

---

## **⚙️ Installation**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/AnshiGupta1/Coin_Oracle.git
cd Coin_Oracle
```

### **2️⃣ Create a Virtual Environment**  
```sh
python -m venv env
# Activate the virtual environment:
# Windows:
env\Scripts\activate  
# macOS/Linux:
source env/bin/activate  
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up API Key**  
Create a `.env` file in the project root directory and add your **Together API key**:  
```ini
TOGETHER_API_KEY=your_api_key_here
```

### **5️⃣ Run the Application**  
```sh
streamlit run app.py
```

---

## **📂 Project Structure**  
```plaintext
Coin_Oracle/
├── app.py           # Main application
├── crypto_agent.py  # AI insights powered by Together API
├── utils.py         # Helper functions for data processing and visualization
├── config.py        # Configuration settings
├── requirements.txt # Dependencies
└── README.md        # Project documentation
```

---

## **🛠 Technologies Used**  

- **[Streamlit](https://streamlit.io/)** – For building the app interface.  
- **[Pandas](https://pandas.pydata.org/)** – For data manipulation.  
- **[Matplotlib](https://matplotlib.org/)** – For data visualization.  
- **[Together API](https://www.together.xyz/)** – For AI insights with the **LLaMA model**.  
- **[Requests](https://docs.python-requests.org/)** – For API data fetching.  

---
