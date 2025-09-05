🍲 RasaBharat – Recipe Generator (Amma Cheti Vontalu)
📌 Project Overview

RasaBharat is a Streamlit-powered app that generates delicious Telugu recipes based on the ingredients, cooking tools, and time available.
It uses Google Gemini AI to create step-by-step recipes in Telugu language.

🔗 Live Demo: https://a3zabek2hajlvsofxcdpsd.streamlit.app/

✨ Features
🥕 Select ingredients (ఉల్లి, టమోటా, చికెన్, etc.)
🍳 Choose cooking tools (పాన్, కడాయి, ప్రెషర్ కుక్కర్, etc.)
⏰ Set cooking time
📖 Generate step-by-step recipe in Telugu
🎨 Simple, clean UI with Streamlit

⚙ Tech Stack
Frontend/UI: Streamlit
AI Model: Google Gemini (via google-generativeai)
Language: Python 3.9+
Deployment: streamlitcloud

🚀 How to Run Locally

Clone the repo:

git clone https://code.swecha.org/shivanimedamoni/rasabharat.git
cd rasabharat

create and  activate virtual environment
ython -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Linux/Mac

install dependencies
pip install -r requirements.txt

add your gemini api key to 
.streamlit/secrets.toml
GOOGLE_API_KEY = "your_api_key_here"

run the app
streamlit run app.Python

📂 Project Structure
rasobharat/
│── app.py
│── requirements.txt
│── README.md
│── REPORT.md
│── CONTRIBUTING.md
│── CHANGELOG.md
│── LICENSE
│── .gitignore

📜 License

This project is licensed under the MIT License.


