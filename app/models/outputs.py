from pydantic import BaseModel, Field, field_validator


class BaseContentOutput(BaseModel):
    title: str = Field(..., description="Short, catchy title")
    text: str = Field(..., description="Main text content")
    hooks: list[str] = Field(
        ..., min_length=3, max_length=3, description="Exactly 3 hooks"
    )
    ctas: list[str] = Field(
        ..., min_length=2, max_length=2, description="Exactly 2 CTAs"
    )
    hashtags: list[str] = Field(
        ..., min_length=6, max_length=10, description="6-10 hashtags"
    )

    @field_validator("text")
    @classmethod
    def validate_text_length(cls, v: str) -> str:
        words = len(v.split())
        if words < 80 or words > 150:
            raise ValueError(f"Text must be 80-150 words, got {words}")
        return v


class EventContentOutput(BaseContentOutput):
    stories_variant: str | None = Field(None, description="Variant for stories")
    reel_variant: str | None = Field(None, description="Variant for reels")
    carousel_variant: list[str] | None = Field(None, description="Slides for carousel")


class ProjectContentOutput(BaseContentOutput):
    variant_a: str = Field(..., description="A/B test variant A")
    variant_b: str = Field(..., description="A/B test variant B")
    platform_specific_notes: str | None = Field(
        None, description="Platform-specific tips"
    )
