# Đây là file frontend.py, nó chứa code để tạo giao diện cho ứng dụng chat

# Nhập thư viện streamlit để tạo giao diện web
import streamlit as st

# Tạo một lớp để quản lý giao diện chat
class ChatAssistantFrontend:
    def __init__(self):
        """
        Khởi tạo giao diện chat assistant.
        Đặt tiêu đề cho trang web và khởi tạo trạng thái phiên chat.
        """
        # Đặt tiêu đề cho trang web
        st.title("CSKH-StepUpEducation Assistant")
        # Khởi tạo trạng thái cho phiên chat
        self.initialize_session_state()

    def initialize_session_state(self):
        """
        Khởi tạo trạng thái phiên làm việc.
        Tạo một danh sách trống để lưu trữ tin nhắn nếu chưa tồn tại.
        """
        # Tạo một nơi để lưu trữ các tin nhắn trong cuộc trò chuyện
        # Nếu chưa có tin nhắn nào, tạo một danh sách trống
        if "messages" not in st.session_state: 
            st.session_state.messages = []

    def display_chat_history(self):
        """
        Hiển thị lịch sử chat.
        Lặp qua tất cả tin nhắn trong phiên làm việc và hiển thị chúng trong giao diện.
        """
        # Hiển thị tất cả các tin nhắn đã có trong cuộc trò chuyện
        for message in st.session_state.messages:
            # Tạo một khung chat cho mỗi tin nhắn
            with st.chat_message(message["role"]):
                # Hiển thị nội dung tin nhắn
                st.markdown(message["content"])

    def get_user_input(self):
        """
        Lấy đầu vào từ người dùng.
        
        Returns:
            str: Câu hỏi hoặc tin nhắn của người dùng.
        """
        # Tạo một ô nhập liệu để người dùng đặt câu hỏi
        return st.chat_input("What is your question?")

    def display_user_message(self, message):
        """
        Hiển thị tin nhắn của người dùng.
        
        Args:
            message (str): Nội dung tin nhắn của người dùng.
        """
        # Hiển thị tin nhắn của người dùng trong khung chat
        st.chat_message("user").markdown(message)

    def display_assistant_message(self, message):
        """
        Hiển thị tin nhắn của trợ lý.
        
        Args:
            message (str): Nội dung tin nhắn của trợ lý.
        """
        with st.chat_message("assistant"):
            try:
                st.markdown(message)
            except Exception as e:
                st.error(f"Error displaying message: {str(e)}")

    def display_error_message(self, message):
        """
        Hiển thị thông báo lỗi.
        
        Args:
            message (str): Nội dung thông báo lỗi.
        """
        # Hiển thị thông báo lỗi nếu có vấn đề xảy ra
        with st.chat_message("assistant"):
            st.error(message)

    def update_chat_history(self, role, content):
        """
        Cập nhật lịch sử chat với tin nhắn mới.

        Args:
            role (str): Vai trò của người gửi tin nhắn ('user' hoặc 'assistant').
            content (str): Nội dung tin nhắn.
        """
        # Thêm tin nhắn mới vào lịch sử cuộc trò chuyện
        # Nếu chưa có lịch sử, tạo một danh sách mới
        if "messages" not in st.session_state:
            st.session_state.messages = []
        # Thêm tin nhắn mới vào cuối danh sách
        st.session_state.messages.append({"role": role, "content": content})

    def get_chat_history(self):
        """
        Lấy toàn bộ lịch sử chat hiện tại.
        
        Returns:
            list: Danh sách các tin nhắn trong lịch sử chat.
        """
        # Lấy toàn bộ lịch sử cuộc trò chuyện hiện tại
        return st.session_state.messages

    def clear_chat_history(self):
        """
        Xóa toàn bộ lịch sử chat.
        Được sử dụng khi bắt đầu một cuộc trò chuyện mới.
        """
        # Xóa toàn bộ lịch sử cuộc trò chuyện khi bắt đầu cuộc trò chuyện mới
        st.session_state.messages = []
