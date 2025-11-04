from app.agents.base import BaseAgent
from app.models.inputs import ProjectInput
from app.models.outputs import ProjectContentOutput
from app.prompts import PROJECT_SYSTEM_PROMPT, PROJECT_USER_PROMPT


class ProjectAgent(BaseAgent[ProjectInput, ProjectContentOutput]):
    def get_system_prompt(self) -> str:
        return PROJECT_SYSTEM_PROMPT

    def build_user_prompt(self, input_data: ProjectInput) -> str:
        return PROJECT_USER_PROMPT.format(
            name=input_data.name,
            context=input_data.context,
            platform=input_data.platform,
            description=input_data.description,
            other_details=input_data.other_details or "none",
        )

    def get_output_schema(self) -> type[ProjectContentOutput]:
        return ProjectContentOutput
