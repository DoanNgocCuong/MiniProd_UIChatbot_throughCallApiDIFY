from backend_package.Threading_ExtendedChatAssistant_class_useCheckTenantAccessToken import ExtendedChatAssistant_Threading
import os
from dotenv import load_dotenv
import sys
import uuid

# Load environment variables
load_dotenv()

# Add the parent directory to sys.path to import config.py
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import config

class ChatAssistantBackend:
    """
    This class is used to handle the backend logic for the chat assistant.
    Use ExtendedChatAssistant_Threading class from Threading_ExtendedChatAssistant_class_useCheckTenantAccessToken.py
    ExtendedChatAssistant_Threading class is extended from ChatAssistant class in ChatAssistant_class.py
    """
    def __init__(self, api_url, api_key, lark_app_token, lark_table_id):
        self.API_URL = api_url
        self.API_KEY = api_key
        self.LARK_APP_TOKEN = lark_app_token
        self.LARK_TABLE_ID = lark_table_id
        
        # Initialize the ExtendedChatAssistant_Threading class
        self.assistant = ExtendedChatAssistant_Threading(
            self.API_URL,
            self.API_KEY,
            self.LARK_APP_TOKEN,
            self.LARK_TABLE_ID,
        )
        self.conversation_id = None

    def start_new_conversation(self):
        """
        Start a new conversation and return the conversation ID.
        """
        # Generate a new conversation ID if it doesn't exist
        if not self.conversation_id:
            self.conversation_id = str(uuid.uuid4())
        # Set the current conversation ID for the assistant
        # Khi ấn F5
        self.assistant.current_conversation_id = self.conversation_id
        return self.conversation_id

    def chat(self, prompt):
        """
        Chat with the assistant and return the response.
        """
        # Nếu conversation_id không có trong st.session_state thì khởi tạo conversation_id
        if not self.conversation_id:
            self.start_new_conversation()
        # Set the current conversation ID for the assistant
        self.assistant.current_conversation_id = self.conversation_id
        return self.assistant.chat(prompt)

# Example usage
if __name__ == "__main__":
    backend = ChatAssistantBackend() # Khởi tạo backend
    while True:
        prompt = input(
            "Enter your question (or type 'exit' to quit, 'new' to start a new conversation): "
        )
        if prompt.lower() == 'exit':
            break
        elif prompt.lower() == 'new':
            print(backend.start_new_conversation())
            continue
        result = backend.chat(prompt)
        print(result)
