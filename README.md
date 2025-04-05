# 🧠 ELI5 Bot

**ELI5 Bot** is an AI-powered chatbot that explains any concept at different difficulty levels, including "Explain Like I'm 5 (ELI5)", Intermediate, and Expert. It uses a local LLM (Mistral-7B Instruct GGUF) and Wikipedia-based context to provide human-like, personalized explanations.

## 🚀 Features

- 🤖 Local LLM using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- 🧠 Difficulty level selector: ELI5, Intermediate, Expert
- 📚 Wikipedia context fetch using `wikipedia` Python package
- 🗣️ Streamlit web UI with intuitive interface
- 🔌 Offline-capable after initial setup

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/Siddheshdumre/eli5-bot.git
cd eli5-bot
```

### 2. Create virtual environment and install dependencies
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
```

### 3. Download the Mistral model
Place the `mistral-7b-instruct-v0.1.Q4_K_M.gguf` model inside the `models/` folder.

You can download it from Hugging Face:  
[TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

Folder structure should be like:
```
eli5-bot/
├── app.py
├── models/
│   └── mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

### 4. Run the chatbot in CLI mode
```bash
python app.py
```

### 5. Or Launch Streamlit App
```bash
streamlit run app.py
```

## 📘 How It Works

1. Takes a user question via UI.
2. Fetches a brief Wikipedia summary.
3. Passes the question and summary to a local LLM.
4. The LLM generates a response based on selected difficulty.

## 🧪 Sample Questions

- What is a black hole?
- Explain deadlocks in OS.
- What is inflation in economics?
- What is DNA?
- How does Wi-Fi work?

## 📁 Folder Structure

```
eli5-bot/
├── app.py                # Main chatbot code (CLI + Streamlit)
├── models/               # Place your GGUF model here
├── README.md             # You're reading this!
└── requirements.txt      # Python dependencies
```

## 🤖 Model Used

- **Mistral-7B Instruct (Q4_K_M)** from [TheBloke's HF repo](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)
- Loaded locally via llama-cpp-python

## 📌 To-Do / Future Improvements

- [x] Add difficulty levels
- [ ] Add voice input/output
- [ ] Enable visual answer mode (images, diagrams)
- [ ] Deploy on Hugging Face / Streamlit Cloud
- [ ] Add memory or chat history

## 📄 License

This project is for educational purposes only.
