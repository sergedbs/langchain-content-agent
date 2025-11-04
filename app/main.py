import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.models.inputs import EventInput
from schemas import BaseOutput
from router import *

from app.agents import EventAgent

# Ce vrei sa postezi pe social media, despre un proiect sau un eveniment?
post_type_event = "eveniment de tehnologie"
post_type_project = "proiect de sustenabilitate"

# Pentru event:
# Denumirea eventului
event_name = "GLIA Tech Summit 2025"

# Agenda sau descrierea scurta a eventului
event_description = (
    "Un eveniment de top care aduce impreuna lideri din industria tehnologiei "
    "pentru a discuta cele mai recente inovatii si tendinte."
)

# Tipul postarii (si optional platforma)
event_post_type = "stories si postare pe facebook"

# Alte detalii (ton, CTA, etc), optional
event_other_details = "ton prietenos si informativ"

# Pentru project:
# Denumirea proiectului
project_name = "GLIA Pre-Accelerator 2025"

# Contextul sau descrierea scurta a proiectului (lansare / reminder / follow-up / testimonial / noutate)
project_description = (
    "Lansarea programului de pre-accelerare destinat startup-urilor din domeniul tehnologiei, "
    "oferind mentorat, resurse si oportunitati de networking."
)

# Plaftorma si/sau tipul postarii
project_post_type = "postare LinkedIn"

# Alte detalii (ton, CTA, etc), optional
project_other_details = "ton profesional si motivant, cu un apel la actiune clar"


def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        print("Missing OPENAI_API_KEY in .env")
        return

    print(f"Using model: {model_name}")

    model = ChatOpenAI(model=model_name, temperature=0.7)

    post_type = route(post_type_event, model)
    print(f"Post type: {post_type}")

    result = EventAgent(ChatOpenAI(model="gpt-4o-mini")).generate(
        EventInput(
            name="Test Event",
            description="A test event for tech",
            post_type="post",
            platform="instagram",
            other_details="ton prietenos si informativ",
        )
    )

    content = result.model_dump_json(indent=2, ensure_ascii=False)
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
