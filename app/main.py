from typing import Optional, Union
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from app.config import get_settings
from app.models.inputs import EventInput, ProjectInput
from app.models.outputs import EventContentOutput, ProjectContentOutput
from app.agents import EventAgent, ProjectAgent
from app.examples import ALL_EXAMPLES
from app.router import route

load_dotenv()


def create_llm(
    model: Optional[str] = None, temperature: Optional[float] = None
) -> ChatOpenAI:
    settings = get_settings()
    return ChatOpenAI(
        model=model or settings.openai_model,
        temperature=temperature or settings.temperature,
    )


def generate_event_content(
    name: str,
    description: str,
    post_type: str,
    platform: str,
    other_details: str = "",
    llm: Optional[ChatOpenAI] = None,
) -> EventContentOutput:
    if llm is None:
        llm = create_llm()

    agent = EventAgent(llm)
    event_input = EventInput(
        name=name,
        description=description,
        post_type=post_type,
        platform=platform,
        other_details=other_details,
    )
    return agent.generate(event_input)


def generate_project_content(
    name: str,
    context: str,
    platform: str,
    description: str,
    other_details: str = "",
    llm: Optional[ChatOpenAI] = None,
) -> ProjectContentOutput:
    if llm is None:
        llm = create_llm()

    agent = ProjectAgent(llm)
    project_input = ProjectInput(
        name=name,
        context=context,
        platform=platform,
        description=description,
        other_details=other_details,
    )
    return agent.generate(project_input)


# Temporarily. For demo only.
def generate_from_example(
    example: dict, llm: Optional[ChatOpenAI] = None
) -> Union[EventContentOutput, ProjectContentOutput]:
    if llm is None:
        llm = create_llm()

    text = f"{example.get('name', '')} {example.get('description', '')}"
    content_type = route(text, llm)

    if content_type == "EVENT":
        return generate_event_content(llm=llm, **example)
    else:
        return generate_project_content(llm=llm, **example)


def run_demo():
    print("=== LangChain Content Agent Demo ===\n")

    llm = create_llm()

    for i, example in enumerate(ALL_EXAMPLES, 1):
        print(f"[{i}/{len(ALL_EXAMPLES)}] Processing: {example['name']}")

        try:
            result = generate_from_example(example, llm)

            text_preview = (
                result.text[:80] + "..." if len(result.text) > 80 else result.text
            )
            print(f"  Text: {text_preview}")

            if hasattr(result, "hooks"):
                print(f"  Hooks: {len(result.hooks)}")
            if hasattr(result, "ctas"):
                print(f"  CTAs: {len(result.ctas)}")
            if hasattr(result, "hashtags"):
                print(f"  Hashtags: {len(result.hashtags)}")

            print()

        except Exception as e:
            print(f"  Error: {e}\n")


if __name__ == "__main__":
    run_demo()
