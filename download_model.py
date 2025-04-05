import os
import requests

model_url = "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
save_path = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

os.makedirs("models", exist_ok=True)

print("Downloading model...")
response = requests.get(model_url, stream=True)
with open(save_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print("✅ Model downloaded successfully.")
