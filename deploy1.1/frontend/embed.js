// frontend/embed.js
function initChatbot(options = {}) {
    const defaultOptions = {
        position: 'right',
        width: '350px',
        height: '500px',
        theme: 'light'
    };

    const config = {...defaultOptions, ...options};
    
    const iframe = document.createElement('iframe');
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
}

window.initChatbot = initChatbot; 