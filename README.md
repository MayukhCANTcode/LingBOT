# Multilingual AI Content Copilot

A Streamlit-based AI application that enables users to generate, rewrite, translate, and convert text into speech using Large Language Models (LLMs). The application integrates the OpenRouter API for AI-powered text generation and gTTS for speech synthesis.

---

## Features

- AI-powered content generation
- Content rewriting with different tones and styles
- Multilingual text translation
- Text-to-Speech (TTS) using gTTS
- MP3 audio download
- Clean and interactive Streamlit interface

---

## Tech Stack

- Python
- Streamlit
- OpenRouter API
- gTTS
- python-dotenv

---

## Project Structure

```text
multilingual-ai-content-copilot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── modules/
│   ├── content_generator.py
│   ├── content_rewriter.py
│   ├── translator.py
│   └── text_to_speech.py
│
├── assets/
│   └── screenshots/
│
└── output/
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MayukhCANTcode/Multilingual-AI-Content-Copilot.git

cd Multilingual-AI-Content-Copilot
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

You can obtain an API key from **https://openrouter.ai/**.

### 5. Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Usage

1. Generate AI content from a prompt.
2. Rewrite existing content in different writing styles.
3. Translate text into multiple languages.
4. Convert text into speech.
5. Download the generated speech as an MP3 file.

---

## Screenshots

### Home Page

(Add screenshot)

### Content Generation

(Add screenshot)

### Translation

(Add screenshot)

### Text-to-Speech

(Add screenshot)

---

## Future Enhancements

- Support for multiple LLM providers
- Speech-to-Text
- Document upload (PDF/DOCX)
- Prompt templates
- Chat history
- User authentication

---

## Requirements

- Python 3.10+
- OpenRouter API Key
- Internet connection

---

## Author

**Mayukh Das**

Electronics & Instrumentation Engineering  
National Institute of Technology Silchar

GitHub: https://github.com/MayukhCANTcode
