import streamlit as st

from modules.content_generator import generate_article
from modules.content_rewriter import rewrite_content
from modules.translator import translate_content

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Multilingual AI Content Copilot",
    page_icon="",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "generated_content" not in st.session_state:
    st.session_state.generated_content = ""

if "translated_content" not in st.session_state:
    st.session_state.translated_content = ""

if "audio_bytes" not in st.session_state:
    st.session_state.audio_bytes = None

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title(" Multilingual AI Content Copilot")

st.markdown("""
Generate, Rewrite, Translate and Convert Content to Speech using AI.

### Features
✅ AI Content Generation  
✅ Content Rewriting  
✅ Multilingual Translation  
✅ Text To Speech  
✅ MP3 Download
""")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Content Settings")

content_type = st.sidebar.selectbox(
    "Content Type",
    [
        "Blog",
        "LinkedIn Post",
        "Podcast Script",
        "YouTube Script"
    ]
)

tone = st.sidebar.selectbox(
    "Tone",
    [
        "Professional",
        "Casual",
        "Friendly",
        "Persuasive"
    ]
)

language = st.sidebar.selectbox(
    "Language",
    [
        "English"
    ]
)

# ==================================================
# SECTION 1 : CONTENT GENERATION
# ==================================================

st.divider()

st.subheader(" Generate Content")

prompt = st.text_area(
    "Enter Topic",
    placeholder="Example: AI Agents"
)

if st.button("Generate Content"):

    if prompt:

        with st.spinner("Generating Content..."):

            st.session_state.generated_content = generate_article(
                topic=prompt,
                content_type=content_type,
                tone=tone,
                language=language
            )

        st.success("Content Generated Successfully!")

if st.session_state.generated_content:

    st.subheader("Generated Content")

    st.write(st.session_state.generated_content)

# ==================================================
# SECTION 2 : CONTENT REWRITER
# ==================================================

st.divider()

st.subheader(" Rewrite Content")

rewrite_format = st.selectbox(
    "Convert To",
    [
        "LinkedIn Post",
        "YouTube Script",
        "Podcast Script",
        "Blog"
    ]
)

if st.button("Rewrite"):

    if not st.session_state.generated_content:
        st.warning("Please generate content first.")
        st.stop()

    with st.spinner("Rewriting Content..."):

        rewritten = rewrite_content(
            content=st.session_state.generated_content,
            target_format=rewrite_format,
            tone=tone
        )

    st.success("Content Rewritten Successfully!")

    st.subheader("Rewritten Content")

    st.write(rewritten)

# ==================================================
# SECTION 3 : TRANSLATION
# ==================================================

st.divider()

st.subheader("Translate Content")

target_language = st.selectbox(
    "Translate To",
    [
        "Hindi",
        "Tamil",
        "Telugu",
        "Malayalam",
        "Kannada",
        "Marathi",
        "German",
        "French",
        "Spanish",
        "Italian",
        "Portuguese"
    ]
)

if st.button("Translate"):

    if not st.session_state.generated_content:
        st.warning("Please generate content first.")
        st.stop()

    with st.spinner("Translating Content..."):

        st.session_state.translated_content = translate_content(
            content=st.session_state.generated_content,
            target_language=target_language
        )

    st.success("Translation Completed!")

if st.session_state.translated_content:

    st.subheader(f"Translated Content ({target_language})")

    st.write(st.session_state.translated_content)

# ==================================================
# SECTION 4 : TEXT TO SPEECH
# ==================================================

st.divider()

st.subheader(" Text To Speech")

if st.button("Generate Audio"):

    if not st.session_state.translated_content:
        st.warning("Please translate content first.")
        st.stop()

    from modules.tts import generate_speech

    with st.spinner("Generating Audio..."):

        output_file = generate_speech(
            st.session_state.translated_content
        )

        with open(output_file, "rb") as audio_file:
            st.session_state.audio_bytes = audio_file.read()

    st.success("Audio Generated Successfully!")

# Audio persists after reruns

if st.session_state.audio_bytes:

    st.audio(st.session_state.audio_bytes)

    st.download_button(
        label="⬇ Download Audio",
        data=st.session_state.audio_bytes,
        file_name="generated_audio.mp3",
        mime="audio/mpeg"
    )
