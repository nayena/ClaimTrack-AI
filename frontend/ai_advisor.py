import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
#this is the key: AIzaSyDtFPzBdghJYQVVfBqzHs6OZp32xLvCvY4
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Fixed typo: GenerativeModel instead of GerativeModel
model = genai.GenerativeModel("gemini-1.0-pro")  # Updated model name

# Fixed typo: title instead of tittle
st.title("ClaimTrack AI Advisor")
st.caption("Powered by Google Gemini")
st.write("Have any additional questions about the insurance claims process? Ask our AI advisor!")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Function to translate roles between Gemini API and Streamlit Terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize the chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chat history
for message in st.session_state.chat_session.history:
    # Fixed typo: chat_message instead of chet_message
    # Fixed typo: message instead of mesage
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask away!...")
if user_prompt:
    # Add user message and display it
    # Fixed typo: prompt instead of promt
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to chat and display it
    # Fixed typo: session_state instead of session.state
    # Fixed typo: user_prompt instead of user.prompt
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)