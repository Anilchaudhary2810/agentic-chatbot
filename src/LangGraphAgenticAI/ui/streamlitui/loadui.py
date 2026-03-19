import streamlit as st
import os

from src.LangGraphAgenticAI.ui.uiconfigfile import Config  

class LoadStreamlitUI: 
    def __init__(self): 
        self.config = Config() 
        self.user_controls = {}  
    
    def load_streamlit_ui(self): 
        st.set_page_config(
            page_title=self.config.page_title(),
            layout="wide"
        ) 
        
        st.header(self.config.page_title())  
              
        with st.sidebar: 
            llm_options = self.config.get_llm_options() 
            usecase_options = self.config.get_usecase_options()
            
            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox(
                "Select LLM", llm_options
            )

            if self.user_controls["selected_llm"].lower() == "groq":
                model_options = self.config.get_groq_model_options()
                
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Select Model", model_options
                )

                api_key = st.text_input("API Key", type="password")
                self.user_controls["GROQ_API_KEY"] = api_key

                if api_key:
                    st.session_state["GROQ_API_KEY"] = api_key
                else:
                    st.warning(
                        "Please enter a valid GROQ API key. "
                        "Get it from: https://console.groq.com/keys"
                    )

            # Use case selection
            self.user_controls["selected_usecases"] = st.selectbox(
                "Select Use Case", usecase_options
            )

        return self.user_controls