SYSTEM_PROMPT = """Ești un copywriter social media senior pentru brandul GLIA.
Scrii texte scurte, clare, energice, cu focus pe impact, comunitate, educație și tech.
Respectă cerințele de lungime și structura.
Limbă: română.
"""

GENERIC_PROMPT = ("""
    Genereaza continut pentru tipul de postare {post_type} despre {name}.
    Descriere: {description}
    Platforma/Tip postare: {post_platform}
    Alte detalii: {other_details}
    Returneaza raspunsul in format JSON
    {{
        "title": "short title",
        "text": "2-3 sentences of text in Romanian"
        "hooks": ["list", "of", "hooks"],
        "ctas": ["list", "of", "ctas"],
        "hashtags": ["list", "of", "hashtags"]
    }}
    Fara nicio eplicare sau oricare detaliu, doar JSON curat.""")

FIND_POST_TYPE_PROMPT = ("""
    Determine if the following text is about an EVENT or a PROJECT.
    Respond with only 'EVENT', 'PROJECT', or 'NONE'.
    Text: '''{text}'''
    """)