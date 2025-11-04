import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from prompts import GENERIC_PROMPT
from schemas import BaseOutput


def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        print("Missing OPENAI_API_KEY in .env")
        return

    print(f"Using model: {model_name}")

    model = ChatOpenAI(model=model_name, temperature=0.7)

    prompt = ChatPromptTemplate.from_template(GENERIC_PROMPT)

    agent = prompt | model
    result = agent.invoke({})

    content = result.content.strip()
    print("\nModel output:\n", content)

    try:
        data = json.loads(content)
        output = BaseOutput(**data)
    except json.JSONDecodeError:
        print("Model didn’t return valid JSON.")
        return
    except Exception as e:
        print(f"Validation failed: {e}")
        return

    print("\nParsed JSON:")
    print(output.model_dump_json(indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
