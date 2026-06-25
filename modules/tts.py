import os
from gtts import gTTS


def generate_speech(
    text,
    output_file="outputs/output.mp3"
):
    # Create the outputs directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    tts = gTTS(
        text=text,
        lang="en"
    )

    tts.save(output_file)

    return output_file
