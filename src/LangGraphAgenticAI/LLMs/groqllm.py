from langchain_groq import ChatGroq


def get_groq_llm(model_name: str, api_key: str) -> ChatGroq:
    return ChatGroq(
        model=model_name,
        api_key=api_key,
        temperature=0.2,
    )
