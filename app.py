import streamlit as st
from codeT5_use import codeT5_predict_optimize, codeT5_predict_secure
from T5_use import T5_predict_optimize, T5_predict_secure

# Streamed response emulator

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

        response = st.write_stream(codeT5_predict_secure(prompt))
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})