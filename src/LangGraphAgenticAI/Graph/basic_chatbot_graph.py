from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from src.LangGraphAgenticAI.Nodes.basic_chatbot_node import build_basic_chatbot_node
from src.LangGraphAgenticAI.state.chat_state import ChatState


def build_basic_chatbot_graph(llm: BaseChatModel) -> Any:
    graph_builder = StateGraph(ChatState)
    graph_builder.add_node("chatbot", build_basic_chatbot_node(llm))

    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    return graph_builder.compile(checkpointer=MemorySaver())
