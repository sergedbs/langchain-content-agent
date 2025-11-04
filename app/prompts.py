GENERIC_PROMPT = ("""
    Generate a short text for a social media post.
    Returns JSON exactly in the format:
    {{
        "title": "short creative title",
        "text": "2-3 sentences of text in Romanian"
        "hooks": ["list", "of", "hooks"],
        "ctas": ["list", "of", "ctas"],
        "hashtags": ["list", "of", "hashtags"]
    }}
    No explanations, just JSON.""")