from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import uuid

app = Flask(__name__)
CORS(app, resources={
    r"/send_message": {"origins": "http://localhost:25040"}
})

class ChatMemory:
    def __init__(self):
        self.conversations = {}

    def add_message(self, user_id, message, conversation_id):
        """
        Add message to conversation history.
        """
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []
        self.conversations[conversation_id].append(message)

    def get_history(self, conversation_id):
        """
        Get conversation history by conversation_id.
        """
        return self.conversations.get(conversation_id, [])

    def send_message(self, user_id, message, conversation_id=None):
        """
        Send message to API and maintain conversation history.
        - First chat: send empty conversation_id="" to Bavaan API
        - Next chats: send existing conversation_id to maintain context
        """
        # Lượt chat đầu: conversation_id là None hoặc rỗng
        if not conversation_id:
            api_conversation_id = ""  # Gửi rỗng cho API Bavaan
        else:
            # Lượt chat tiếp theo: validate conversation_id đã có
            try:
                uuid.UUID(conversation_id)
                api_conversation_id = conversation_id
            except ValueError:
                raise ValueError("Invalid conversation_id format. Must be a valid UUID.")

        # Lưu message vào history
        self.add_message(user_id, message, conversation_id or "temp")
        history = self.get_history(conversation_id or "temp")

        response = requests.post(
            'https://studio.bavaan.ai/v1/chat-messages',
            headers={
                'Authorization': 'Bearer app-W6h9SjqlbnO7W9nFjE3lC5dI',
                'Content-Type': 'application/json'
            },
            data=json.dumps({
                "inputs": {
                    "context": " "
                },
                "query": message,
                "response_mode": "blocking",
                "conversation_id": api_conversation_id,  # Gửi "" cho lượt đầu
                "user": user_id
            })
        )
        
        response_data = response.json()
        
        # Nếu là lượt chat đầu, cập nhật conversation_id từ response
        if not conversation_id:
            new_conversation_id = response_data.get("conversation_id")
            # Cập nhật history với conversation_id mới
            if "temp" in self.conversations:
                self.conversations[new_conversation_id] = self.conversations.pop("temp")
            print(f"New conversation_id: {new_conversation_id}")
            print(response_data)
            return {
                "conversation_id": new_conversation_id,
                "response": response_data
            }
        print(f"Conversation_id: {conversation_id}")
        print(response_data)
        return {
            "conversation_id": conversation_id,
            "response": response_data
        }

# Create ChatMemory instance
chat_memory = ChatMemory()

@app.route('/send_message', methods=['POST'])
def handle_message():
    try:
        data = request.json
        user_id = data.get('user_id')
        message = data.get('message')
        conversation_id = data.get('conversation_id')
        
        response = chat_memory.send_message(user_id, message, conversation_id)
        return jsonify(response)
    except ValueError as e:
        return jsonify({"code": "invalid_param", "message": str(e), "params": "conversation_id"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)