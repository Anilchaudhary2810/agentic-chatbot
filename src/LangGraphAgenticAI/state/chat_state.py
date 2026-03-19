from typing import Any

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, NotRequired, TypedDict


class ChatState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    metadata: NotRequired[dict[str, Any]]
