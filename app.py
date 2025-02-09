import streamlit as st
import langchainChatbot as lcc




def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""
    
    

def set_send_input():
    st.session_state.send_button = True
    clear_input_field()
    



def main():
    st.set_page_config(page_title = "PDF's and more!!" , page_icon = "🤖")
    
    st.title("Multimodal local Chat Application")
    chat_container = st.container()
    
    
    if "send_input" not in st.session_state:
        st.session_state.send_input = False
    if "user_question" not in st.session_state:    
        st.session_state.user_question = ""
    
    user_input = st.text_input("Enter your message" , key = "user_input" , on_change= set_send_input)
    
    send_button = st.button("Send" , key = "send_button")
    # if st.button("Send"):
    #     st.session_state.send_input = True
    #     clear_input_field()
    
    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
        
            llm_response = "This is a response from the LLM model"
            
            with chat_container:
                st.chat_message("user").write(st.session_state.user_question)
                st.chat_message("ai").write("Here is the answer")
        

if __name__ == "__main__":
    main()