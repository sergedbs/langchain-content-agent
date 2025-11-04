from langchain_openai import ChatOpenAI

from app.prompts import ROUTING_PROMPT

EVENT_KEYWORDS = {
    "eveniment",
    "event",
    "conferință",
    "conferinta",
    "workshop",
    "recap",
    "webinar",
    "summit",
    "forum",
    "meetup",
    "seminar",
}

PROJECT_KEYWORDS = {
    "proiect",
    "project",
    "parteneriat",
    "inițiativă",
    "initiativa",
    "accelerator",
    "pre-accelerator",
    "program",
    "partnership",
}


def detect_by_keywords(text: str) -> str | None:
    text_lower = text.lower()

    has_event = any(keyword in text_lower for keyword in EVENT_KEYWORDS)
    has_project = any(keyword in text_lower for keyword in PROJECT_KEYWORDS)

    if has_event and not has_project:
        return "EVENT"
    elif has_project and not has_event:
        return "PROJECT"

    return None


def detect_by_ai(text: str, llm: ChatOpenAI) -> str | None:
    prompt = ROUTING_PROMPT.format(text=text)
    response = llm.invoke(prompt)
    result = str(response.content).strip().upper()

    if result in {"EVENT", "PROJECT"}:
        return result

    return None


def route(text: str, llm: ChatOpenAI | None = None) -> str:
    if not text or not text.strip():
        raise ValueError("Text cannot be empty")

    content_type = detect_by_keywords(text)

    if content_type is not None:
        return content_type

    if llm is not None:
        content_type = detect_by_ai(text, llm)

        if content_type is not None:
            return content_type

    raise ValueError(
        "Could not determine content type. "
        "Please specify if this is an EVENT or PROJECT."
    )
