const chatWindow = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

let conversationId = ""; // Quản lý conversation_id cho hội thoại

// Hàm hiển thị tin nhắn
function displayMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.innerText = text;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight; // Tự động cuộn xuống cuối
}

// Gửi tin nhắn đến server
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Hiển thị tin nhắn người dùng
    displayMessage(message, 'user');
    userInput.value = ""; // Xóa nội dung input

    // Gửi tin nhắn đến backend
    const response = await fetch('http://127.0.0.1:25039/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: 'abc-123',
            message: message,
            conversation_id: conversationId // Gửi conversation_id nếu có
        })
    });

    const data = await response.json();
    conversationId = data.conversation_id; // Cập nhật conversation_id

    // Hiển thị phản hồi từ bot
    displayMessage(data.response.answer, 'bot');
}

// Xử lý sự kiện nhấn nút
sendButton.addEventListener('click', sendMessage);

// Xử lý sự kiện nhấn Enter
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
