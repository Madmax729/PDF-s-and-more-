import streamlit as st

def main():
    st.set_page_config(page_title = "PDF's and more!!" , page_icon = "🤖")
    
    st.title("Multimodal local Chat Application")
    chat_container = st.container()
    
    user_input = st.text_input("Enter your message" , key = "user_input")
    
    send_button = st.button("Send" , key = "send_button")
    
    if send_button:
        llm_response = "This is a response from the LLM model"
        
        with chat_container:
            st.chat_message("user").write(user_input)
            st.chat_message("ai").write("Here is the answer")
    

if __name__ == "__main__":
    main()