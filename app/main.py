import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from prompts import GENERIC_PROMPT, SYSTEM_PROMPT
from schemas import BaseOutput
from router import *

# Ce vrei sa postezi pe social media, despre un proiect sau un eveniment?
post_type_event = "eveniment de tehnologie"
post_type_project = "proiect de sustenabilitate"

# Pentru event:
# Denumirea eventului
event_name = "GLIA Tech Summit 2025"

# Agenda sau descrierea scurta a eventului
event_description = ("Un eveniment de top care aduce impreuna lideri din industria tehnologiei "
                     "pentru a discuta cele mai recente inovatii si tendinte.")

# Tipul postarii (si optional platforma)
event_post_type = "stories si postare pe facebook"

# Alte detalii (ton, CTA, etc), optional
event_other_details = "ton prietenos si informativ"

# Pentru project:
# Denumirea proiectului
project_name = "GLIA Pre-Accelerator 2025"

# Contextul sau descrierea scurta a proiectului (lansare / reminder / follow-up / testimonial / noutate)
project_description = ("Lansarea programului de pre-accelerare destinat startup-urilor din domeniul tehnologiei, "
                       "oferind mentorat, resurse si oportunitati de networking.")

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

    system = ChatPromptTemplate.from_template(SYSTEM_PROMPT)
    user = ChatPromptTemplate.from_template(GENERIC_PROMPT)
    prompt = ChatPromptTemplate.from_messages([system, user])

    agent = prompt | model
    result = agent.invoke({
        "post_type": post_type,
        "name": event_name if post_type == "EVENT" else project_name,
        "description": event_description if post_type == "EVENT" else project_description,
        "post_platform": event_post_type if post_type == "EVENT" else project_post_type,
        "other_details": event_other_details if post_type == "EVENT" else project_other_details
    })

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
