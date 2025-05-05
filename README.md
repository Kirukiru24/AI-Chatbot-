# 🤖 Gemini Chatbot with Google Generative AI API

A simple AI chatbot built in Python using the Gemini (Google Generative AI) API. Users can interact with the chatbot via a web interface and receive intelligent, real-time responses based on their input.

---

## 🚀 Features

- Interactive web UI using **Gradio**
- Real-time text responses powered by **Google Gemini Pro**
- Clean and simple user interface
- Secure API key handling via `.env` file

---

## 🧰 Technologies Used

- Python 3.9+
- [Gradio](https://gradio.app/) – UI framework
- [Google Generative AI API (Gemini)](https://ai.google.dev)
- `google-generativeai` Python SDK
- `python-dotenv` for environment variable management

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-chatbot.git
cd AI_chatbot

# Create a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your Gemini API Key
Create a .env file in the root directory and add:

env
Copy
Edit
GOOGLE_API_KEY=your_gemini_api_key_here
Replace your_gemini_api_key_here with your actual API key from https://makersuite.google.com/app/apikey
🧪 Running the App
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:7860 in your browser to use the chatbot.

📁 Project Structure
bash
Copy
Edit
gemini-chatbot/
│
├── app.py             # Main application
├── requirements.txt   # Python dependencies
├── .env               # Gemini API key (DO NOT SHARE)
├── .gitignore
└── README.md
🛡️ Disclaimer
This project is for educational/demo purposes only. Do not expose your API key publicly. Monitor usage to avoid unexpected charges.

💡 License
MIT License

🙌 Acknowledgments
Google Generative AI

Gradio
⬇
