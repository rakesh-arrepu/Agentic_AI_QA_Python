# file: test_ollama.py
from langchain_ollama import ChatOllama

llm = ChatOllama(model="mistral:7b")
resp = llm.invoke("Hello from Ollama via LangChain! Keep it to one sentence.")
print(resp.content)