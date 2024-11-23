// frontend/embed.js
function initChatbot(options = {}) {
    const defaultOptions = {
        position: 'right',
        width: '350px',
        height: '500px',
        theme: 'light'
    };

    const config = {...defaultOptions, ...options};
    
    const toggleButton = document.createElement('button');
    toggleButton.id = 'chatbot-toggle';
    toggleButton.innerHTML = '💬';
    toggleButton.style.cssText = `
        position: fixed;
        bottom: 20px;
        ${config.position}: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        color: white;
        font-size: 24px;
        cursor: pointer;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        z-index: 999999;
        display: none;
    `;
    
    document.body.appendChild(toggleButton);

    const iframe = document.createElement('iframe');
    iframe.id = 'chatbot-iframe';
    iframe.src = `http://localhost:25040/index.html?t=${Date.now()}`;
    iframe.allow = "microphone *";
    iframe.style.cssText = `
        position: fixed;
        bottom: 20px;
        ${config.position}: 20px;
        width: ${config.width};
        height: ${config.height};
        border: none;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        z-index: 999999;
    `;
    
    document.body.appendChild(iframe);

    // Toggle button click handler
    toggleButton.addEventListener('click', () => {
        iframe.contentWindow.postMessage({ type: 'showChatbot' }, '*');
        iframe.style.display = 'block';
        toggleButton.style.display = 'none';
    });

    // Listen for close message from iframe
    window.addEventListener('message', (event) => {
        if (event.data && event.data.type === 'closeChatbot') {
            iframe.style.display = 'none';
            toggleButton.style.display = 'block';
        }
    });

    window.chatbot = {
        sendMessage: (message) => {
            iframe.contentWindow.postMessage({ type: 'sendMessage', message }, '*');
        }
    };
}

window.initChatbot = initChatbot;