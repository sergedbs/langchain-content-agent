from app.agents.base import BaseAgent
from app.models.inputs import EventInput
from app.models.outputs import EventContentOutput
from app.prompts import EVENT_SYSTEM_PROMPT, EVENT_USER_PROMPT


class EventAgent(BaseAgent[EventInput, EventContentOutput]):
    def get_system_prompt(self) -> str:
        return EVENT_SYSTEM_PROMPT

    def build_user_prompt(self, input_data: EventInput) -> str:
        return EVENT_USER_PROMPT.format(
            name=input_data.name,
            description=input_data.description,
            post_type=input_data.post_type,
            platform=input_data.platform or "general",
            other_details=input_data.other_details or "none",
        )

    def get_output_schema(self) -> type[EventContentOutput]:
        return EventContentOutput
