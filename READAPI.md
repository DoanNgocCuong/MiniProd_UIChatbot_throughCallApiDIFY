
### Qwen2.5 - API
```bash
curl -X POST 'https://mentor-dev.fpt.ai/math-centerpiece-model' \
-H 'Content-Type: application/json' \
-d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a great assistant."
    },
    {
      "role": "user",
      "content": "Calculate 100 + 400 - 250. Just output the answer."
    }
  ]
}'
```
### API Basic RAG: 

```bash

### 1. **Thông tin API**
- **Endpoint**: `http://103.253.20.13:9225/flashrag/rag/custom/generate`
- **Method**: `POST`

### 2. **Request JSON**
Dưới đây là cấu trúc JSON mà bạn cần gửi trong yêu cầu:

```json
{
    "api_key": "<API KEY>",  // Thay thế bằng API Key của bạn
    "text": "Khách hàng đã gặp vấn đề gì khi giao tiếp",
    "top_k": 5,
    "return_doc": false,
    "prompt": [
        {
            "role": "system",
            "content": "You are an intelligent assistant. Please answer the question based on content of knowledge base. When all knowledge base content is irrelevant to the question, your answer must include the sentence 'The answer you are looking for is not found in the knowledge base!'. Answers need to consider chat history. Knowledge base content is as following:\n{{REFERENCE}}"
        },
        {
            "role": "user",
            "content": "The question is: '{{TEXT}}'.\nAnswer only the question and do not output any other words."
        }
    ],
    "format_content": "Doc {{INDEX}}: {{TITLE}}\n {{CONTENT}}\n"
}
```

cRUL 
```bash
curl --location 'http://103.253.20.13:9225/flashrag/rag/custom/generate' \
--header 'Content-Type: application/json' \
--data '{
    "api_key": "KB-20240930155359526614ElULtm4UAWTWqIpO0VFwAHUN9ntITvHe",
    "text": "Khách hàng đã gặp vấn đề gì khi giao tiếp",
    "top_k": 5,
    "return_doc": false,
    "prompt": [
        {
            "role": "system",
            "content": "You are an intelligent assistant. Please answer the question based on content of knowledge base. When all knowledge base content is irrelevant to the question, your answer must include the sentence '\''The answer you are looking for is not found in the knowledge base!'\''. Answers need to consider chat history. Knowledge base content is as following:\n{{REFERENCE}}"
        },
        {
            "role": "user",
            "content": "The question is: '\''{{TEXT}}'\''. Answer only the question and do not output any other words."
        }
    ],
    "format_content": "Doc {{INDEX}}: {{TITLE}}\n {{CONTENT}}\n"
}'
```


### 3. **Response JSON**
Khi bạn gửi yêu cầu, bạn sẽ nhận được phản hồi với cấu trúc như sau:

```json
{
    "status": 0,
    "msg": "Success",
    "result": {
        "pred_answer_list": "Phản xạ chậm, ngập ngừng, ậm ừ khi nói, sử dụng các từ đệm (filter words) khi nói.",
        "retrieval_result": null
    }
}
```

### 4. **Các trường thông tin**
- **api_key**: Yêu cầu, kiểu String.
- **text**: Yêu cầu, kiểu String.
- **top_k**: Yêu cầu, kiểu int.
- **document_name**: Tùy chọn, kiểu String.
- **priority_document_name**: Tùy chọn, kiểu String.
- **return_doc**: Tùy chọn, kiểu Boolean.
- **prompt**: Tùy chọn, kiểu PromptJson.
- **format_content**: Tùy chọn, kiểu String.

```

