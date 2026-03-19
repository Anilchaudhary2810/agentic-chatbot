from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel

from src.LangGraphAgenticAI.state.chat_state import ChatState


def build_basic_chatbot_node(llm: BaseChatModel):
    def chatbot_node(state: ChatState) -> dict[str, Any]:
        response = llm.invoke(state["messages"])
        return {"messages": [response]}

    return chatbot_node
