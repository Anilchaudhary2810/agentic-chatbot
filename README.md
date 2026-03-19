# Agentic Chatbot (LangGraph + Groq)

A Streamlit chatbot following a LangGraph project structure.

## Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the app:

```bash
streamlit run app.py
```

3. In the sidebar:
- Select `Groq`
- Choose a model
- Paste your Groq API key

## Notes

- Chat flow is implemented with LangGraph: `State -> Chatbot Node -> End`.
- Memory is kept per model in Streamlit session state using a LangGraph in-memory checkpointer.
