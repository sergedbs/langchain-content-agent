EVENT_KEYWORDS = {"eveniment", "event", "conferință", "conferinta", "workshop", "recap",
                  "webinar", "summit", "forum", "meetup"}
PROJECT_KEYWORDS = {"projects", "project", "proiect", "parteneriat", "inițiativă", "initiativa",
                    "accelerator", "pre-accelerator", "program"}


def detect_event_type(text: str) -> str | None:
    t = text.lower()
    if any(h in t for h in EVENT_KEYWORDS) and not any(h in t for h in PROJECT_KEYWORDS):
        return "EVENT"
    if any(h in t for h in PROJECT_KEYWORDS) and not any(h in t for h in EVENT_KEYWORDS):
        return "PROJECT"
    return None

def detect_event_type_using_ai(text: str, ai_model) -> str | None:
    prompt = (f"Determine if the following text is about an EVENT or a PROJECT. "
              f"Respond with only 'EVENT', 'PROJECT', or 'NONE'.\n\nText: '''{text}'''")
    response = ai_model.generate_text(prompt)
    result = response.strip().upper()
    if result in {"EVENT", "PROJECT"}:
        return result
    return None

def route(text: str, ai_model=None) -> str | None:
    event_type = detect_event_type(text)
    if event_type is None and ai_model is not None:
        event_type = detect_event_type_using_ai(text, ai_model)
    return event_type