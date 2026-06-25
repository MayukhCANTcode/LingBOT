from modules.gemini_helper import generate_content


def generate_article(
    topic,
    content_type,
    tone,
    language
):

    prompt = f"""
    Create a {content_type}

    Topic: {topic}

    Tone: {tone}

    Language: {language}

    Make it engaging and well structured.
    """

    return generate_content(prompt)
