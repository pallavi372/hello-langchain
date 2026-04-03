from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    project = os.getenv('GOOGLE_CLOUD_PROJECT')

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        vertexai=True,
        project=project
    )

    country = input("Enter the country: ")

    messages = [
        SystemMessage(content="You are a social teacher for a Primary School. Explain interesting facts also."),
        HumanMessage(content=f"What is the capital of {country}?")
    ]

    response = llm.invoke(messages)
    print("\nAnswer:\n", response.content)


if __name__ == "__main__":
    main()