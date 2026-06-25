from modules.gemini_helper import generate_content


def translate_content(
    content,
    target_language
):

    prompt = f"""
    Translate the following content into {target_language}.

    Preserve:
    - Meaning
    - Tone
    - Formatting

    Content:

    {content}
    """

    return generate_content(prompt)
