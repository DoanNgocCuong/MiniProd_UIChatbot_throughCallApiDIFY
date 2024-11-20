Cấu trúc thư mục

```
APIBasicRAG_chatbot/
│
├── backend_package/
│   ├── ChatAssistant_class.py                      # Your ChatAssistant base class
│   ├── ExtendedChatAssistant_class.py              # Extended class with threading
│   ├── createRecord_checkTenantAccessToken.py      # Function to log records to Lark Base
│   ├── createRecord_tenantAccessToken.py           # Tenant Access Token related file
│   ├── get_tenantAccessToken_funct.py              # Functions to get tenant access token
│   ├── Threading_ExtendedChatAssistant_class_useCheckTenantAccessToken.py # Threaded extended assistant using tenant token
│   └── refresh_user_access_token.md                # Markdown file for refreshing access tokens
│
├── frontend_package/
│   ├── frontend.py                                 # Frontend interface file using Streamlit
│
├── main.py                                         # Main file to run the Streamlit app
├── .env                                            # Environment variables (API_KEY, API_URL, etc.)
└── config.py                                       # Configurations for Lark and other constants
```

Ensure you are running the Streamlit app from the correct directory. You should be in the `APIBasicRAG_chatbot` directory when you run the command:

```bash
streamlit run main.py
```

### HOW TO RUN - LOCAL 
1. Create virtual env sử dụng `python -m venv .venv`
2. Truy vào vào `venv` bằng run Terminal: `.venv/Scripts/activate`
3. Install requirements.txt sử dụng `pip install -r requirements.txt`
4. Run test thử 1 số hàm độc lập xem còn hoạt động không, nhất là hàm backend chính `Threading_ExtendedChatAssistant`
5. `cd` vào `APIBasicRAG_chatbot`, cd vào `deploy2` sau đó `streamlit run main.py`


------------------------------
### HOW TO DEPLOY: 

1. Cuong have created a Dockerfile in your project root:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "main.py"]
```

2. Build the Docker image:

```bash
docker build -t apibasicrag-chatbot .
```

3. Run the Docker container:

```bash
docker run -p 8501:8501 apibasicrag-chatbot
```

Docker không tự động đọc file .env trừ khi bạn chỉ định rõ ràng. Bạn cần phải sử dụng file .env khi chạy Docker container. Sửa đổi lệnh chạy Docker container để nó sử dụng file .env:
```bash
docker run --env-file .env -p 8501:8501 apibasicrag-chatbot
```


----------------
chú ý : 
1. THAY .env và config.py 
2. SET UP ĐÚNG CÁC TRƯỜNG DỮ LIỆU TRONG BASE:
- Cụ thể bài này sẽ toàn là text gồm các cột: chat_id, conversation_id, system_prompt, user_input, assistant_response
