# main.py

import streamlit as st
from frontend_package.frontend import ChatAssistantFrontend
from backend_package.backend import ChatAssistantBackend
import os
import config

# Initialize the Streamlit interface
frontend = ChatAssistantFrontend()

# Load environment variables for backend configurations
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
LARK_APP_TOKEN = config.APP_BASE_TOKEN
LARK_TABLE_ID = config.BASE_TABLE_ID

# Error checking for necessary API configurations
if not API_URL or not API_KEY or not LARK_APP_TOKEN or not LARK_TABLE_ID:
    st.error("Missing API or Lark configurations. Please check your environment variables and config file.")
else:
    # Initialize the backend
    if 'backend' not in st.session_state: # Kiểm tra xem backend đã được khởi tạo chưa
        st.session_state.backend = ChatAssistantBackend(API_URL, API_KEY, LARK_APP_TOKEN, LARK_TABLE_ID)

    # Ensure conversation_id is initialized only once per session
    # Nếu conversation_id không có trong st.session_state thì khởi tạo conversation_id
    if 'conversation_id' not in st.session_state:
        # Gọi hàm start_new_conversation() để khởi tạo conversation_id
        # Khi gọi hàm start_new_conversation() thì conversation_id sẽ được khởi tạo và lưu vào st.session_state.conversation_id
        st.session_state.conversation_id = st.session_state.backend.start_new_conversation()
    
    # Display chat history in the frontend
    frontend.display_chat_history()

    # Get user input from frontend
    user_input = frontend.get_user_input()

    if user_input:
        # Display the user's message in the frontend
        frontend.display_user_message(user_input)
        
        # Update the chat history with user message
        frontend.update_chat_history("user", user_input)

        # Get assistant's response from the backend
        assistant_response = st.session_state.backend.chat(user_input)

        # Display assistant's response in the frontend
        frontend.display_assistant_message(assistant_response)

        # Update the chat history with assistant's message
        frontend.update_chat_history("assistant", assistant_response)

        # Force Streamlit to rerun to update the display
        st.rerun()
