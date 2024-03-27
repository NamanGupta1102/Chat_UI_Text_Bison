import streamlit as st
import random
import time
import json
import requests
from LLM_Model import predict
def palm_reccomend(buggy_code):
  # api_key = "AIzaSyCuf-_Tq7gKStezexKTa2i2G8Ectg9xw8Q" #saachi key
  api_key = "AIzaSyBmjhopUEEOHLgBwvn0r36e3tsHUqOnEfA"
  time.sleep(3)
  prompt = {
      "text": buggy_code
    #    + '''\nGive a recommendation for making this code more secure:\n
    #           Give me the most important 3 points to secure this code.\n
    #           Answer in three sentences only, and be specific.'''
  }

  # Create JSON request body
  raw = json.dumps({"prompt": prompt})

  # Send POST request
  url = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"
  params = {"key": api_key}
  response = requests.post(url, params=params, data=raw)

  # Check for successful response
  if response.status_code == 200:
      try:
        # Process the response (e.g., extract the generated text)
        data = response.json()
        # print(data['candidates'][0]['output'])
        print(data)
        return data['candidates'][0]['output']
      except:
        print("Not working")
        print(data)
        return "000_Didnt Work"
  else:
      print(f"Error: {response.status_code}")
      return("000_Error")


# Streamed response emulator
def response_generator(prompt):
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    response = palm_reccomend(prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})