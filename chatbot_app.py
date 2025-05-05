import streamlit as st
import google.generativeai as genai

# Configure Gemini with your API Key
genai.configure(api_key="AIzaSyAkDB4CAe4jp-pngWc3s1Wfw1y0JHuxvlQ")  # Replace with your key

# Create a Gemini chat model
for model in genai.list_models():
    print(model.name)
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Gemini AI Chatbot")
st.markdown("Type your message and get a response from Google's Gemini model.")

# Maintain chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text input
user_input = st.text_input("You:", placeholder="Ask me anything...", key="input")

# Handle send
if st.button("Send") and user_input.strip() != "":
    try:
        response = model.generate_content(user_input)
        assistant_reply = response.text

        # Append to chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Gemini", assistant_reply))

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Gemini:** {message}")
