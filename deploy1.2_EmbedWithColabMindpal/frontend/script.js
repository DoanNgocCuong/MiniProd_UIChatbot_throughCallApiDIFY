// frontend/script.js
const chatWindow = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

let conversationId = "";

const BACKEND_URL = 'http://localhost:25039';

function displayMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.innerText = text;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendMessage(message) {
    if (!message) return;

    // Hiển thị tin nhắn
    displayMessage(message, 'user');

    try {
        const response = await fetch(`${BACKEND_URL}/send_message`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id: 'abc-123',
                message: message,
                conversation_id: conversationId
            })
        });

        const data = await response.json();
        conversationId = data.conversation_id;
        displayMessage(data.response.answer, 'bot');
    } catch (error) {
        console.error('Error sending message:', error);
        displayMessage('Sorry, there was an error processing your message.', 'bot');
    }
}

// Xử lý tin nhắn từ parent window
// Xử lý tin nhắn từ parent window
window.addEventListener('message', (event) => {
    if (event.data?.type === 'showChatbot') {
        const chatContainer = document.querySelector('.chat-container');
        if (chatContainer) {
            chatContainer.style.display = 'flex';  // Đảm bảo hiển thị lại đúng layout
        }
    }
    if (event.data?.type === 'sendMessage') {
        const message = event.data.message;
        // Đảm bảo container được hiển thị trước khi gửi tin nhắn
        const chatContainer = document.querySelector('.chat-container');
        if (chatContainer) {
            chatContainer.style.display = 'flex';
        }
        sendMessage(message);
    }
});

// Xử lý input từ người dùng
sendButton.addEventListener('click', () => {
    const message = userInput.value.trim();
    if (message) {
        sendMessage(message);
        userInput.value = '';
    }
});

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const message = userInput.value.trim();
        if (message) {
            sendMessage(message);
            userInput.value = '';
        }
    }
});


// Lắng nghe sự kiện click để đóng chatbot
document.getElementById('close-chatbot').addEventListener('click', () => {
    const chatContainer = document.querySelector('.chat-container');
    if (chatContainer) {
        chatContainer.style.display = 'none';
    } else {
        console.error('Chat container not found!');
    }

    window.parent.postMessage({ type: 'closeChatbot' }, '*');
});

