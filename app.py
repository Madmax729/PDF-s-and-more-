import streamlit as st
from llm_chains import load_normal_chain
from langchain.memory import StreamlitChatMessageHistory
from langchain.memory import ChatMessageHistory



def load_chain(chat_history):
    return load_normal_chain(chat_history)

def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""
    

def set_send_input():
    st.session_state.send_input = True
    clear_input_field()
    
def main():
    st.set_page_config(page_title="PDF's and more!!", page_icon="🤖")
    
    st.title("Multimodal Local Chat Application")
    chat_container = st.container()
    
    if "send_input" not in st.session_state:
        st.session_state.send_input = False
    if "user_question" not in st.session_state:    
        st.session_state.user_question = ""
        
    chat_history = StreamlitChatMessageHistory(key ="history") 
    # chat_history = ChatMessageHistory()

    llm_chain = load_chain(chat_history)  
    
    
    
    
    user_input = st.text_input("Enter your message", key="user_input", on_change=set_send_input)
    
    send_button_pressed = st.button("Send", key="send_button")
    
    if send_button_pressed or st.session_state.send_input:
        if st.session_state.user_question.strip() != "":
            llm_response = "This is a response from the LLM model"  # Replace with actual LLM call
            
            with chat_container:
                st.chat_message("user").write(st.session_state.user_question)
                llm_response = llm_chain.run(st.session_state.user_question)
                st.chat_message("ai").write(llm_response)
                st.session_state.user_question = ""

            # Reset send_input flag after processing
            st.session_state.send_input = False

if __name__ == "__main__":
    main()
