Deploy1: From QA Assistant to Chatbot Friendly with Memory
Deploy2: Log conversation history to Larkbase

### Run: 
- Mẹo chung: Khi build UI, bạn ấn: pip install streamlit => Auto được đề xuất tạo .env (cùng với auto cài requirements.txt)
```bash
.venv\Scripts\activate
```

- Với cấu trúc thư mục như này thì khi deploy trên Streamlit Cloud, 


Dựa trên cấu trúc thư mục của bạn, việc chạy **`deploy2/main.py`** hoàn toàn hợp lý vì file này là điểm chính để khởi chạy ứng dụng **Streamlit** của bạn. Tuy nhiên, bạn cần chắc chắn rằng:

1. **File `.env`** đã được cấu hình đúng trong thư mục **`deploy2/`**. File `.env` này nên chứa các biến môi trường quan trọng như **API_KEY**, **API_URL**, và các thông tin cần thiết khác mà ứng dụng sử dụng. Nếu thiếu các biến quan trọng, ứng dụng có thể gặp lỗi khi kết nối tới API hoặc các dịch vụ khác.
    
2. **Các đường dẫn đến các module** như **`backend_package`** và các file cấu hình (**`config.py`**) đã được cấu hình chính xác trong **`main.py`**. Điều này đảm bảo rằng khi chạy **`main.py`**, ứng dụng có thể tìm và sử dụng đúng các thư viện và hàm được định nghĩa trong các file Python khác (như **`ChatAssistant_class.py`** và **`ExtendedChatAssistant_class.py`**).
    
3. **Tất cả các dependency trong `requirements.txt`** hoặc các package cần thiết đã được cài đặt trong môi trường của bạn. Nếu sử dụng **Streamlit Cloud**, các thư viện này sẽ tự động được cài từ `requirements.txt`, nhưng nếu sử dụng Docker hoặc server khác, bạn cần đảm bảo môi trường đã cài đặt đúng các thư viện.
    

### Kiểm tra trước khi deploy:

- Kiểm tra kết nối đến **Lark Base** và các hàm liên quan đến việc lấy **Tenant Access Token** từ **`createRecord_checkTenantAccessToken.py`**.
- Đảm bảo rằng các phần liên quan đến frontend (`frontend.py`) hoạt động tốt và giao diện người dùng được render đúng cách với Streamlit.

Nếu các phần này đều ổn, bạn có thể chạy:

bash

Copy code

`streamlit run deploy2/main.py`

### Lưu ý:

Nếu gặp lỗi về **biến môi trường**, hãy kiểm tra lại file `.env` hoặc sử dụng thư viện **`python-dotenv`** để chắc chắn rằng các biến môi trường đã được load đúng cách.
