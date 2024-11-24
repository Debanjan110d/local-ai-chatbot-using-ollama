from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template= """
Answeer the question below
Here is the conversation history:{context}
Question: {question}
Answer:
"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain=prompt | model

def handel_conversation():
    context = ""
    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Chatbot:", result)
        context += f"\nYou: {user_input}\nChatbot: {result}\n"

# result = chain.invoke({"context": "", "question": "What is your name?"})

if __name__ == "__main__":
    handel_conversation()
