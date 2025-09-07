# file: test_openai.py
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
resp = llm.invoke("Hello from OpenAI via LangChain! Keep it to one sentence.")
print(resp.content)
