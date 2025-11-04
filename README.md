# LangChain Content Agent

AI-powered Python tool that automatically generates social media content for events and projects using LangChain and OpenAI.

## Overview

This tool uses specialized AI agents to generate platform-optimized social media content in Romanian. It distinguishes between two content types:

- **Events** (conferences, workshops, summits) - Generates content with GLIA brand tone
- **Projects** (accelerators, partnerships, initiatives) - Generates content adapted to each project's brand

## How It Works

1. **Content Routing**: Automatically detects whether input is an event or project using keyword matching and AI fallback
2. **Agent Selection**: Routes to the appropriate specialized agent (EventAgent or ProjectAgent)
3. **Content Generation**: Generates comprehensive social media content including:
   - Title and main text (80-150 words)
   - 3 hooks and 2 CTAs
   - 6-10 hashtags
   - Platform-specific variants (Stories, Reels, Carousel for events; A/B test variants for projects)

## Architecture

- **Template Method Pattern**: BaseAgent defines generation workflow; specialized agents implement prompts and schemas
- **Strategy Pattern**: Different agents for different content types
- **Dependency Injection**: LLM can be injected for testing and reuse
- **Structured Output**: Uses Pydantic models for type-safe, validated outputs

## Requirements

- Python 3.11+
- OpenAI API key

## Installation

```bash
# Clone repository
git clone https://github.com/sergedbs/langchain-content-agent.git
cd langchain-content-agent

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

## Usage

### Option 1: Run Demo with Examples

The simplest way to see the tool in action:

```bash
python app/run_demo.py
```

This will process the examples in `app/examples.py` and display generated content for each.

### Option 2: Customize Examples

Edit `app/examples.py` to add your own events or projects:

```python
EXAMPLES = [
    {
        "name": "Your Event Name",
        "description": "Event description",
        "post_type": "carousel",  # stories, reel, carousel, post
        "platform": "Instagram",
        "other_details": "additional details"
    },
    {
        "name": "Your Project Name",
        "context": "lansare",  # lansare, reminder, follow-up, testimonial, noutate
        "platform": "LinkedIn",
        "description": "Project description",
        "other_details": "additional details"
    }
]
```

Then run `python app/run_demo.py` to see results.

### Option 3: Use as Library

Import and use the generation functions in your own code:

```python
from app.main import generate_event_content, generate_project_content, create_llm

# Create LLM instance (reusable)
llm = create_llm()

# Generate event content
result = generate_event_content(
    name="Tech Summit 2025",
    description="Annual technology conference",
    post_type="carousel",
    platform="Instagram",
    other_details="energetic tone",
    llm=llm
)

print(result.title)
print(result.text)
print(result.hooks)
print(result.ctas)
print(result.hashtags)
print(result.carousel_variant)

# Generate project content
result = generate_project_content(
    name="Pre-Accelerator Program",
    context="lansare",
    platform="LinkedIn",
    description="Startup acceleration program",
    other_details="professional tone",
    llm=llm
)

print(result.title)
print(result.text)
print(result.variant_a)  # A/B test variant A
print(result.variant_b)  # A/B test variant B
print(result.platform_specific_notes)
```

### Option 4: Auto-Detection with Router

Let the tool automatically detect content type:

```python
from app.main import generate_content, create_llm

llm = create_llm()

# Automatically detects if it's an event or project
result = generate_content(
    {
        "name": "Workshop AI",
        "description": "Workshop about AI integration",
        "post_type": "stories",
        "platform": "Instagram"
    },
    llm=llm
)
```

## Configuration

Edit `app/config.py` or set environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: Model to use (default: "gpt-4o-mini")
- `TEMPERATURE`: Generation temperature (default: 0.7)
- `MIN_WORDS`: Minimum word count (default: 50)
- `MAX_WORDS`: Maximum word count (default: 200)

## Output Structure

### Event Content

- Title (max 10 words)
- Text (80-150 words)
- 3 hooks
- 2 CTAs
- 6-10 hashtags
- Stories variant (40-50 words)
- Reel variant (natural script)
- Carousel variant (3-5 slide titles)

### Project Content

- Platform-adapted title
- Text (80-150 words)
- 3 platform-specific hooks
- 2 CTAs with deadlines
- 6-10 platform-specific hashtags
- Variant A (professional, data-driven)
- Variant B (emotional, story-driven)
- Platform-specific strategy notes

## Disclaimer

The example content and prompts in this project were created with the assistance of large language models (LLMs). The tool itself uses OpenAI's API to generate social media content dynamically based on user input.
