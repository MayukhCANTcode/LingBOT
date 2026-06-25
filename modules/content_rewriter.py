from modules.gemini_helper import generate_content


def rewrite_content(
    content,
    target_format,
    tone
):

    prompt = f"""
    Rewrite the following content.

    Target Format: {target_format}

    Tone: {tone}

    Content:
    {content}

    Keep the meaning unchanged but adapt it
    to the target format.
    """

    return generate_content(prompt)
