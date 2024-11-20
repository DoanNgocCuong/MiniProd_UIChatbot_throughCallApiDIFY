import json
import requests

class ChatMemory:
    def __init__(self):
        self.conversations = {}

    def add_message(self, user_id, message, conversation_id):
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []
        self.conversations[conversation_id].append(message)

    def get_history(self, conversation_id):
        return self.conversations.get(conversation_id, [])

    def send_message(self, user_id, message, conversation_id):
        self.add_message(user_id, message, conversation_id)
        history = self.get_history(conversation_id)
        
        # Gửi yêu cầu đến API
        response = requests.post(
            'https://studio.bavaan.ai/v1/chat-messages',
            headers={
                'Authorization': 'Bearer app-W6h9SjqlbnO7W9nFjE3lC5dI',
                'Content-Type': 'application/json'
            },
            data=json.dumps({
                "inputs": {
                    "context": " ".join(history)
                },
                "query": message,
                "response_mode": "blocking",
                "conversation_id": conversation_id,
                "user": user_id
            })
        )
        return response.json()