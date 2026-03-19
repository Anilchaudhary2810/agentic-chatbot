from typing import Any

import streamlit as st
from langchain_core.messages import HumanMessage

from src.LangGraphAgenticAI.Graph.basic_chatbot_graph import build_basic_chatbot_graph
from src.LangGraphAgenticAI.LLMs.groqllm import get_groq_llm


class DisplayResultStreamlit:
    def __init__(self, user_controls: dict[str, Any]):
        self.user_controls = user_controls

    @staticmethod
    def _state_key(prefix: str, model_name: str) -> str:
        safe_model_name = model_name.replace("/", "_").replace("-", "_")
        return f"{prefix}_{safe_model_name}"

    def _get_or_create_graph(self, model_name: str, api_key: str) -> Any:
        graph_key = self._state_key("chat_graph", model_name)

        if graph_key not in st.session_state:
            llm = get_groq_llm(model_name=model_name, api_key=api_key)
            st.session_state[graph_key] = build_basic_chatbot_graph(llm=llm)

        return st.session_state[graph_key]

    def _render_history(self, messages: list[dict[str, str]]) -> None:
        for message in messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def render(self) -> None:
        selected_llm = self.user_controls.get("selected_llm", "").lower()
        selected_usecase = self.user_controls.get("selected_usecases", "")

        if selected_usecase.lower() != "basic chatbot":
            st.info("Please select 'Basic Chatbot' use case.")
            return

        if selected_llm != "groq":
            st.info("This template currently supports Groq only.")
            return

        api_key = self.user_controls.get("GROQ_API_KEY") or st.session_state.get("GROQ_API_KEY")
        model_name = self.user_controls.get("selected_groq_model", "")

        if not api_key:
            st.info("Enter your GROQ API key in the sidebar to start chatting.")
            return

        if not model_name:
            st.info("Please select a Groq model from the sidebar.")
            return

        messages_key = self._state_key("chat_messages", model_name)
        thread_key = self._state_key("thread_id", model_name)

        if messages_key not in st.session_state:
            st.session_state[messages_key] = []

        if thread_key not in st.session_state:
            st.session_state[thread_key] = f"thread_{model_name}"

        self._render_history(st.session_state[messages_key])
        user_prompt = st.chat_input("Ask something...")

        if not user_prompt:
            return

        st.session_state[messages_key].append({"role": "user", "content": user_prompt})

        with st.chat_message("user"):
            st.markdown(user_prompt)

        graph = self._get_or_create_graph(model_name=model_name, api_key=api_key)
        config = {"configurable": {"thread_id": st.session_state[thread_key]}}

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = graph.invoke({"messages": [HumanMessage(content=user_prompt)]}, config=config)
                assistant_text = str(result["messages"][-1].content)
                st.markdown(assistant_text)

        st.session_state[messages_key].append({"role": "assistant", "content": assistant_text})
