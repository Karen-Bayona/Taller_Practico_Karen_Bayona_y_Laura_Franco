import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv() 
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=2000, 
    temperature=0,
)

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

prompt = (
    "Explica qué es la 'Inferencia en IA'. "
    "Requisito estricto: tu respuesta debe tener EXACTAMENTE entre 40 y 50 palabras, ni más ni menos. "
    "Cuenta las palabras antes de responder. "
    "Responde en español, solo con el texto de la explicación, sin frases introductorias."
)

print("--- Ejercicio 1: Conexión y Petición Básica ---\n")

chat = client.chats.create(model=MODEL, config=configuration)
response = chat.send_message(prompt)

print("¿Qué es la Inferencia en IA?\n")
print(response.text)
print(f"\nPalabras: {len(response.text.split())}")