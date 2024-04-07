import streamlit as st
from codeT5_use import codeT5_predict_optimize, codeT5_predict_secure
from T5_use import T5_predict_optimize, T5_predict_secure
import json
import requests

from code_editor import code_editor

# Streamed response emulator

st.title("C.O.S.T")

def palm_optimize(buggy_code):
  # api_key = "AIzaSyCuf-_Tq7gKStezexKTa2i2G8Ectg9xw8Q" #saachi key
  api_key = "AIzaSyBmjhopUEEOHLgBwvn0r36e3tsHUqOnEfA"
#   time.sleep(3)
  prompt = {
      "text": buggy_code + '''\nGive a recommendation for making this code more secure:\n
              Give me the most important 3 points to secure this code.\n
              Answer in three sentences only, and be specific.'''
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

def palm_secure(buggy_code):
  # api_key = "AIzaSyCuf-_Tq7gKStezexKTa2i2G8Ectg9xw8Q" #saachi key
  api_key = "AIzaSyBmjhopUEEOHLgBwvn0r36e3tsHUqOnEfA"
#   time.sleep(3)
  prompt = {
      "text": buggy_code + '''\nGive a recommendation for making this code more optimized:\n
              Give me the most important 3 points to optimize this code.\n
              Answer in three sentences only, and be specific.'''
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

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

#secure = st.button("Secure")

#st.code('''hello, world''', language="python", line_numbers=False)

optimize_secure_buttons = [
    {    
         "name": "Secure", 
         "hasText": True, 
         "alwaysOn": True,
         "commands": [["response", "Secure"]],
         "feather": "Lock",
         "style": {
             "top": "0.46rem", 
             "right": "0.4rem"
         }
    },
    {
         "name": "Optimize",
         "hasText": True,
         "alwaysOn": True,
         "commands": [["response", "Optimize"]],
         "feather": "TrendingUp",
         "style": {"top": "0.46rem", "right": "6rem"}
 },
]


# st.write("")
# st.session_state.messages = [{"role": "assistant", "content": "Welcome to cost"}]
if user_response := code_editor('''''', lang="python", buttons = optimize_secure_buttons):
    user_code = user_response["text"][:500]
    # if "messages" not in st.session_state:
    #     st.session_state.messages = []
    # print(user_response)
    if user_response["type"].lower() == 'secure':
        response = codeT5_predict_secure(user_code)
        # st.write(response)
        print(response)
        st.session_state.messages = [{"role": "assistant", "content": response}]
    elif user_response["type"].lower() == 'optimize':
        response = codeT5_predict_optimize(user_code)
        # st.write(response)
        print(response)
        st.session_state.messages = [{"role": "assistant", "content": response}]

 

# Display chat messages from history on app rerun
    for message in st.session_state.messages:
      with st.chat_message(message["role"]):
        st.markdown(message["content"])

    
    # else:
    #     # st.session_state.messages = [{"role": "assistant", "content": "Welcome to cost"}]
    #     response = codeT5_predict_optimize(user_code)
    #     #st.write(response)
    #     print(response)
    #     st.session_state.messages = [{"role": "assistant", "content": response}]
        

    #if user_response["type"].lower() == 'optimize':


#optimize = st.button("Optimize")
# Accept user input
#
#if prompt := st.chat_input("What is up?"):
#    # Add user message to chat history
#
#    st.session_state.messages.append({"role": "user", "content": prompt})
#    # Display user message in chat message container
#    
#    with st.chat_message("user"):
#        st.write(prompt)
#
#    # Display assistant response in chat message container
#    with st.chat_message("assistant"):
#        if 'secure' in prompt.lower():
#            response = codeT5_predict_secure(prompt)
#            st.write(codeT5_predict_secure(prompt))
#        elif 'optimize' in prompt.lower():
#            response = codeT5_predict_optimize(prompt)
#            st.write(response)
#        else:
#            response = codeT5_predict_secure(prompt)
#            st.write(response)
#        # st.session_state.messages.append({"role": "assistant", "content": prompt})
#    
#    # Add assistant response to chat history
#    #working
#    st.session_state.messages.append({"role": "assistant", "content": response})