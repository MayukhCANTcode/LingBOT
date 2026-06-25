from tempfile import NamedTemporaryFile
from gtts import gTTS


def generate_speech(text):
    tts = gTTS(
        text=text,
        lang="en"
    )

    temp_file = NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.close()

    tts.save(temp_file.name)

    return temp_file.name
