import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    temperature=0.7,
    system_instruction="Eres un vendedor amable y experto de una tienda de tecnología. Ayudas a los clientes a encontrar productos, ofreciendo especificaciones claras y un trato cordial."
)

MODEL = "gemini-3.6-flash"

conversation_history = [
    {
        "role": "user", 
        "parts": [{"text": "¿Qué características tiene el portátil Acer Aspire?"}]
    },
    {
        "role": "model", 
        "parts": [{"text": "¡Hola! Con mucho gusto te cuento. El Acer Aspire es ideal para estudio y trabajo: cuenta con un procesador rápido, excelente rendimiento y pantalla de alta definición. ¿Te gustaría saber el precio o algún detalle en específico?"}]
    },
    {
        "role": "user", 
        "parts": [{"text": "¿Tienen tabletas Samsung disponibles?"}]
    },
    {
        "role": "model", 
        "parts": [{"text": "¡Claro que sí! Tenemos excelentes opciones de tabletas Samsung, perfectas para tomar notas, estudiar o ver contenido multimedia. ¿Buscas algún modelo en particular?"}]
    }
]

print("--- Chat de Soporte - Tienda de Tecnología ---")
print("(Escribe 'finalizar' para terminar)\n")

while True:
    user_input = input("Cliente: ")
    
    if user_input.lower() in ["finalizar", "salir", "exit"]:
        print("\nVendedor: ¡Gracias por visitar nuestra tienda de tecnología! Que tengas un excelente día.")
        break

    try:
        conversation_history.append({
            "role": "user",
            "parts": [{"text": user_input}]
        })

        response = client.models.generate_content(
            model=MODEL,
            contents=conversation_history,
            config=configuration
        )
        
        assistant_message = response.text
        
        conversation_history.append({
            "role": "model",
            "parts": [{"text": assistant_message}]
        })

        print(f"\nVendedor: {assistant_message}\n")

    except Exception as e:            
        print(f"Error al procesar la solicitud: {e}")