from pydantic import BaseModel, Field


class EventInput(BaseModel):
    name: str = Field(..., description="Event name")
    description: str = Field(..., description="Event agenda/description")
    post_type: str = Field(..., description="Type: stories/recap/reel/carousel")
    platform: str | None = Field(None, description="Optional platform")
    other_details: str | None = Field(None, description="Additional details, eg. tone")


class ProjectInput(BaseModel):
    name: str = Field(..., description="Project name")
    context: str = Field(..., description="Context: launch/reminder/etc")
    platform: str = Field(..., description="Target platform")
    description: str = Field(..., description="Project description")
    other_details: str | None = Field(None, description="Additional details, eg. tone")
