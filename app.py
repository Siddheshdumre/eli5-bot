import streamlit as st
from llama_cpp import Llama
import wikipedia
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Load Mistral model
llm = Llama(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=6,
    n_gpu_layers=20,
    verbose=False
)

st.set_page_config(page_title="🧠 ELI5 Bot", page_icon="🧠")
st.title("🧠 ELI5 Bot")
st.caption("Explain anything at different difficulty levels.")

# 🎙️ Use microphone
use_voice = st.checkbox("🎙️ Use voice input")

def record_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, could not understand audio.")
        except sr.RequestError:
            st.error("Could not request results.")
    return ""

if use_voice:
    if st.button("🎤 Record Question"):
        user_input = record_voice()
    else:
        user_input = ""
else:
    user_input = st.text_input("🔍 Ask your question:")

difficulty = st.selectbox("📘 Select difficulty level", ["ELI5 (Child)", "Intermediate", "Expert"])

# 🧾 Format option
format_option = st.selectbox("🎨 Answer style", ["Standard", "Storytelling", "Technical Breakdown"])

def get_wikipedia_summary(query):
    try:
        return wikipedia.summary(query, sentences=5)
    except:
        return "Sorry, I couldn’t find anything on that."

def format_prompt(question, context, level, style):
    styles = {
        "ELI5 (Child)": "Explain like I'm 5 years old.",
        "Intermediate": "Explain like you're teaching a teenager.",
        "Expert": "Explain like a computer science professor."
    }

    formats = {
        "Standard": "",
        "Storytelling": " Make it a fun story or use analogies.",
        "Technical Breakdown": " Break down the explanation into bullet points with technical detail."
    }

    return f"""[Context]
{context}

[Task]
{styles[level]}{formats[style]}

Question: {question}

Answer:"""

if user_input:
    with st.spinner("🔎 Fetching background info..."):
        wiki_summary = get_wikipedia_summary(user_input)

    st.subheader("📚 Wikipedia Summary")
    st.write(wiki_summary)

    with st.spinner("🧠 Thinking..."):
        prompt = format_prompt(user_input, wiki_summary, difficulty, format_option)
        response = llm(prompt, max_tokens=512)
        answer = response["choices"][0]["text"].strip()

    st.subheader("👨‍🏫 Answer")
    st.write(answer)

    if st.button("🔊 Speak Answer"):
        speak_text(answer)
