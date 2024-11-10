import sys
import requests
from ollama import Client
import streamlit as st

ollama_url = 'http://localhost:11434'

if requests.get(ollama_url).status_code == 200:
    client = Client(host=ollama_url)
else:
    st.error("Ollama is not running")
    sys.exit(1)

def request(gpt_model, messages):
    response = client.chat(
        model=gpt_model,
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
        stream=True,
    )

    current_reply = ""
    for chunk in response:
        message = chunk['message']
        current_reply += message.get("content", "")

    return current_reply

# Change the title and description
st.title("🌟 Medical Advisor Chatbot 🌟")
st.markdown("""
Welcome to the Medical Advisor Chatbot! 🤖💬  
Here, you can ask questions about health, symptoms, and medical advice.  
**Disclaimer:** This chatbot is not a substitute for professional medical advice.  
Feel free to type your questions below!
""")

if 'messages' not in st.session_state:
    st.session_state.messages = []

if st.session_state.messages:
    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Assistant:** {msg['content']}")

# Set the model name directly to medllama2:7b
model = "medllama2:7b"

# User input form with highlighted question
with st.form(key='input_form'):
    st.markdown("### 🤔 What health question do you have?")
    prompt = st.text_input("Type your question here...", placeholder="e.g., What are the symptoms of diabetes?")
    submit_button = st.form_submit_button(label="Ask") 

# Handle user input
if submit_button and prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    model_response = request(model, st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": model_response})

    st.rerun()  

# Start Over button to reset the conversation
if st.button("Start Over"):
    st.session_state.messages.clear()
    st.rerun()
