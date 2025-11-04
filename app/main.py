import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        print("Missing OPENAI_API_KEY in .env")
        return

    print(f"Using model: {model_name}")

    model = ChatOpenAI(model=model_name, temperature=0.7)

    prompt = ChatPromptTemplate.from_template("""
    Generates a short text for a social media post.
    Returns JSON exactly in the format:
    {{
        "title": "short creative title",
        "text": "2-3 sentences of text in Romanian"
    }}
    No explanations, just JSON.
    """)

    agent = prompt | model
    result = agent.invoke({})

    content = result.content.strip()
    print("\nModel output:\n", content)

    try:
        data = json.loads(content)
        print("\nParsed JSON:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print("\nCould not parse valid JSON, check the model output formatting.")


if __name__ == "__main__":
    main()
