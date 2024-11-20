
- Lấy API Key từ bavaan.ai
- Lấy Workflow ID từ bavaan.ai

1. API Workflow: 
```bash
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
```



POST
/workflows/run

```bash
curl -X POST 'https://studio.bavaan.ai/v1/workflows/run' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "response_mode": "streaming",
    "user": "abc-123"
}'
```



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
