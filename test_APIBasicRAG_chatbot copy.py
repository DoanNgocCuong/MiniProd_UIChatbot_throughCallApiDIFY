import requests
import json
import streamlit as st

url = 'http://103.253.20.13:9225/flashrag/rag/custom/generate'
headers = {
    'Content-Type': 'application/json',
}

st.title("CSKH-StepUpEducation Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is your question?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Prepare the data for the API request
    data = {
        "api_key": "KB-20240930155359526614ElULtm4UAWTWqIpO0VFwAHUN9ntITvHe",
        "text": prompt,
        "top_k": 5,
        "return_doc": False,
        "prompt": [
            {
                "role": "system",
                "content": "You are a friendly and helpful assistant for CSKH-StepUpEducation. Your responses should be natural, engaging, and conversational. Use the knowledge base content to inform your answers, but present the information in a smooth, chatbot-like manner. If the knowledge base doesn't contain relevant information, politely inform the user. Here's the knowledge base content:\n{{REFERENCE}}"
            },
        ] + [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages[-5:]] + [
            {
                "role": "user",
                "content": f"The user asks: '{prompt}'. Please provide a friendly, conversational response that addresses their question while considering the chat history above."
            }
        ],
        "format_content": "Doc {{INDEX}}: {{TITLE}}\n {{CONTENT}}\n"
    }

    print("Sending request with data:", json.dumps(data, indent=2))  # Print request data

    response = requests.post(url, headers=headers, json=data)

    print("Response status code:", response.status_code)  # Print response status code

    if response.status_code == 200:
        result = response.json()
        print("Raw response:", json.dumps(result, indent=2))  # Print raw response
        
        # Extract the response content
        content = result.get('result', {}).get('pred_answer_list', '')
        
        print("Formatted result:", content)  # Print formatted result

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(content)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": content})
    else:
        print("Error response:", response.text)  # Print error response
        with st.chat_message("assistant"):
            st.error(f"Error: {response.status_code} - {response.text}")