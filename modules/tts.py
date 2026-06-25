from gtts import gTTS


def generate_speech(
    text,
    output_file="outputs/output.mp3"
):
    tts = gTTS(
        text=text,
        lang="en"
    )

    tts.save(output_file)

    return output_file
