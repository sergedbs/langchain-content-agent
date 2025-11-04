from pydantic import BaseModel

class BaseOutput(BaseModel):
    title: str
    text: str
    hooks: list[str]
    ctas: list[str]
    hashtags: list[str]