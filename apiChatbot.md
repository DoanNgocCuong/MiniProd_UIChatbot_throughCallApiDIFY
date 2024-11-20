Request
POST
/chat-messages
curl -X POST 'https://studio.bavaan.ai/v1/chat-messages' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "query": "What are the specs of the iPhone 13 Pro Max?",
    "response_mode": "streaming",
    "conversation_id": "",
    "user": "abc-123",
    "files": [
      {
        "type": "image",
        "transfer_method": "remote_url",
        "url": "https://cloud.dify.ai/logo/logo-site.png"
      }
    ]
}'



Response
```json
{
    "workflow_run_id": "djflajgkldjgd",
    "task_id": "9da23599-e713-473b-982c-4328d4f5c78a",
    "data": {
        "id": "fdlsjfjejkghjda",
        "workflow_id": "fldjaslkfjlsda",
        "status": "succeeded",
        "outputs": {
          "text": "Nice to meet you."
        },
        "error": null,
        "elapsed_time": 0.875,
        "total_tokens": 3562,
        "total_steps": 8,
        "created_at": 1705407629,
        "finished_at": 1727807631
    }
}
```


========

1. 
```
curl --location 'https://studio.bavaan.ai/v1/workflows/run' \
--header 'Authorization: Bearer app-iM1ComaH5h7bbALYUNTMAE1Y' \
--header 'Content-Type: application/json' \
--data '{
    "inputs": {
        "transcription": "Đây là nội dung cần phân tích."
    },
    "response_mode": "blocking",
    "user": "unique_user_id",
    "workflow_id": "eb6487f8-39b6-42b6-a10e-5f8162c6b251"
}'



Tại sao workflow thì có workflow_id trong crul  , mà sao chatbot lại không có chatbot_id trong crul mà chỉ có Key. 
```





## 1. **Sự khác biệt giữa Workflow và Chatbot trong API**

Câu hỏi của bạn rất hợp lý! Sự khác biệt giữa việc sử dụng **`workflow_id`** trong Workflow và không sử dụng **`chatbot_id`** trong Chatbot chủ yếu liên quan đến cách API được thiết kế và tổ chức.

---

### **1. Vì sao Workflow cần `workflow_id`?**
- **Workflow là gì?**
  - Một Workflow là một luồng công việc hoặc một tập hợp các bước được định nghĩa trước trong hệ thống, chẳng hạn như xử lý dữ liệu, phân tích hoặc trả lời câu hỏi.
  - Workflow có thể chứa nhiều kịch bản phức tạp với các chức năng khác nhau.

- **Lý do cần `workflow_id`:**
  - **Workflow không duy nhất theo API Key:** 
    - Một tài khoản có thể có nhiều Workflow được định nghĩa. Hệ thống cần biết cụ thể bạn muốn thực thi Workflow nào.
  - **Xác định luồng công việc cụ thể:**
    - `workflow_id` là định danh duy nhất để server biết bạn đang yêu cầu thực thi **luồng công việc nào** trong số các luồng có sẵn của bạn.
  - **Phân biệt giữa các Workflow:**
    - Ví dụ, tài khoản của bạn có thể có hai Workflow:
      - Workflow A: Phân tích giọng nói.
      - Workflow B: Xử lý văn bản.
    - Khi gọi API, bạn cần chỉ định `workflow_id` để server thực thi đúng luồng công việc bạn muốn.

---

### **2. Vì sao Chatbot không cần `chatbot_id`?**
- **Chatbot là gì?**
  - Chatbot là một ứng dụng tương tác, thường sử dụng một bộ xử lý ngôn ngữ tự nhiên (LLM) để trả lời câu hỏi hoặc trò chuyện với người dùng.

- **Lý do không cần `chatbot_id`:**
  - **Chatbot thường đi kèm API Key duy nhất:**
    - Trong hầu hết các trường hợp, **mỗi API Key được liên kết với một chatbot duy nhất** hoặc một cấu hình duy nhất.
    - Hệ thống có thể tự động xác định chatbot liên quan dựa trên **API Key** mà bạn sử dụng.
  - **Không cần phân biệt nhiều chatbot trong cùng một tài khoản:**
    - Nếu tài khoản của bạn chỉ có một chatbot, việc yêu cầu thêm `chatbot_id` là không cần thiết.
    - Nếu tài khoản hỗ trợ nhiều chatbot, thông thường API Key sẽ gắn với từng chatbot cụ thể.

---

### **3. Tóm tắt sự khác biệt**

| **Đặc điểm**               | **Workflow**                                                | **Chatbot**                                                  |
|----------------------------|------------------------------------------------------------|-------------------------------------------------------------|
| **Yêu cầu `workflow_id`**  | Có, vì một tài khoản có thể có nhiều Workflow khác nhau.    | Không, vì mỗi API Key thường gắn liền với một chatbot cụ thể. |
| **Xác định đối tượng**      | Dựa trên `workflow_id` để chọn đúng luồng công việc.         | Dựa trên **API Key**, không cần thêm định danh khác.          |
| **Phạm vi sử dụng**         | Dành cho các quy trình tự động hóa hoặc xử lý phức tạp.      | Tương tác đơn giản, hỏi đáp hoặc hội thoại với AI.           |

---

### **Khi nào cần `chatbot_id` trong Chatbot API?**
Nếu bạn quản lý **nhiều chatbot trên cùng một tài khoản API**, hệ thống có thể yêu cầu bạn cung cấp **`chatbot_id`**. Tuy nhiên, điều này thường không phổ biến vì:
- Các nền tảng chatbot hiện nay thường sử dụng API Key để xác định chatbot liên quan.
- Cấu trúc thiết kế này giúp đơn giản hóa yêu cầu API.

---

Nếu bạn cần thêm thông tin hoặc có thắc mắc khác, cứ hỏi nhé! 😊




## 2. Cách chatbot ghi nhớ hội thoại

Để triển khai khả năng "nhớ hội thoại" cho chatbot dựa trên API mà bạn đang sử dụng, bạn cần sử dụng tham số **`conversation_id`** trong request. Dưới đây là cách hoạt động và hướng dẫn chi tiết:

---

### **1. Cách hoạt động của `conversation_id`**
- **`conversation_id`** là một tham số để xác định và gắn kết các câu hỏi/đáp án trong cùng một phiên hội thoại.
- Khi bạn sử dụng cùng một **`conversation_id`**, API sẽ:
  - Lưu trữ lịch sử hội thoại của phiên đó.
  - Sử dụng ngữ cảnh trước đó để tạo phản hồi tốt hơn.

---

### **2. Triển khai chatbot với khả năng nhớ hội thoại**

#### **Bước 1: Khởi tạo hội thoại mới**
- Gửi một request với **`conversation_id`** trống (`""`).
- API sẽ tự động tạo một **`conversation_id`** mới và trả về trong phản hồi.

**Request ví dụ:**
```bash
curl --location 'https://studio.bavaan.ai/v1/chat-messages' \
--header 'Authorization: Bearer app-W6h9SjqlbnO7W9nFjE3lC5dI' \
--header 'Content-Type: application/json' \
--data '{
    "inputs": {
        "context": "Provide detailed specifications of mobile phones including release date, screen size, and features."
    },
    "query": "What are the specs of the iPhone 13 Pro Max?",
    "response_mode": "blocking",
    "conversation_id": "",
    "user": "abc-123"
}'
```

**Phản hồi:**
```json
{
    "event": "message",
    "conversation_id": "c9ce1859-2e6c-41b6-91ee-56c8f077ac61",
    "message_id": "08702687-8cc1-4523-ab3a-b9d2aecadd2f",
    "created_at": 1732099289,
    "answer": "The iPhone 13 Pro Max has a 6.7-inch display with ..."
}
```

#### **Bước 2: Lưu trữ `conversation_id`**
- Lấy `conversation_id` từ phản hồi và lưu trữ (ví dụ: lưu vào bộ nhớ tạm thời, database, hoặc session của người dùng).

#### **Bước 3: Sử dụng `conversation_id` trong các request tiếp theo**
- Gửi thêm câu hỏi và cung cấp cùng một **`conversation_id`** để tiếp tục hội thoại.

**Request ví dụ:**
```bash
curl --location 'https://studio.bavaan.ai/v1/chat-messages' \
--header 'Authorization: Bearer app-W6h9SjqlbnO7W9nFjE3lC5dI' \
--header 'Content-Type: application/json' \
--data '{
    "inputs": {
        "context": "Provide detailed specifications of mobile phones."
    },
    "query": "How about the battery capacity?",
    "response_mode": "blocking",
    "conversation_id": "c9ce1859-2e6c-41b6-91ee-56c8f077ac61",
    "user": "abc-123"
}'
```

**Phản hồi:**
```json
{
    "event": "message",
    "conversation_id": "c9ce1859-2e6c-41b6-91ee-56c8f077ac61",
    "message_id": "1876abc3-9abc-4758-bbc5-d12345678efg",
    "created_at": 1732099400,
    "answer": "The battery capacity of the iPhone 13 Pro Max is 4352 mAh."
}
```

---

### **3. Triển khai lưu trữ `conversation_id`**
Tùy vào cách bạn triển khai, bạn có thể lưu trữ **`conversation_id`** bằng các phương pháp sau:

#### **a. Lưu trữ tạm thời (In-memory storage):**
- Sử dụng biến tạm thời trong ứng dụng backend của bạn.
- Phù hợp cho các ứng dụng nhỏ hoặc không cần lưu hội thoại lâu dài.

```python
# Ví dụ lưu trữ trong Python
user_sessions = {}

# Khi bắt đầu hội thoại mới
conversation_id = api_response.get("conversation_id")
user_sessions["abc-123"] = conversation_id

# Khi tiếp tục hội thoại
conversation_id = user_sessions.get("abc-123")
```

#### **b. Lưu trữ trong cơ sở dữ liệu:**
- Tạo bảng lưu trữ `user_id` và `conversation_id`.
- Phù hợp cho các ứng dụng lớn, nhiều người dùng.

```sql
CREATE TABLE UserConversations (
    user_id VARCHAR(255) PRIMARY KEY,
    conversation_id VARCHAR(255)
);

-- Khi lưu mới
INSERT INTO UserConversations (user_id, conversation_id)
VALUES ('abc-123', 'c9ce1859-2e6c-41b6-91ee-56c8f077ac61');

-- Khi truy vấn
SELECT conversation_id FROM UserConversations WHERE user_id = 'abc-123';
```

#### **c. Lưu trữ trong session của người dùng:**
- Nếu bạn sử dụng session (như Flask hoặc Django), lưu `conversation_id` trong session.

```python
# Lưu vào session
session["conversation_id"] = api_response.get("conversation_id")

# Lấy từ session
conversation_id = session.get("conversation_id")
```

---

### **4. Triển khai logic cho bot**
1. **Khởi tạo hội thoại mới:**
   - Nếu không có `conversation_id` (lần đầu chat), gửi request với `conversation_id` trống.

2. **Tiếp tục hội thoại:**
   - Nếu có `conversation_id`, gửi kèm trong các request tiếp theo.

3. **Kết thúc hội thoại:**
   - Khi người dùng muốn bắt đầu hội thoại mới, xóa `conversation_id` khỏi bộ nhớ.

---

### **Kết quả**
- Chatbot của bạn sẽ "nhớ" ngữ cảnh hội thoại dựa trên `conversation_id`.
- Người dùng có thể trò chuyện liên tục mà không cần lặp lại thông tin.

Nếu bạn cần hỗ trợ thêm về triển khai, cứ hỏi nhé! 😊