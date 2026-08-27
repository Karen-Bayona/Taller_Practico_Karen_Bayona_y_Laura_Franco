import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import logging

logging.getLogger("google_genai").setLevel(logging.ERROR)

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

client = genai.Client(api_key=API_KEY)


SYSTEM_INSTRUCTION = (
    "Eres un Editor Editorial de prestigio, con décadas de experiencia en medios "
    "reconocidos. Tu criterio es exigente, preciso y profesional. Respondes "
    "siempre en español, sin frases introductorias ni comentarios sobre tu propio "
    "proceso: solo entregas el texto final solicitado."
)


def procesar_articulo(texto, tarea):

    tarea = tarea.lower().strip()

    if tarea == "resumir":
        prompt = (
            "Redacta un resumen ejecutivo del siguiente artículo. "
            "Debe capturar las ideas principales, ser claro y conciso "
            "(entre 80 y 120 palabras), y mantener un tono profesional.\n\n"
            f"ARTÍCULO:\n{texto}"
        )
    elif tarea == "profesionalizar":
        prompt = (
            "Edita el siguiente artículo para que su redacción sea formal, "
            "técnica y profesional, corrigiendo cualquier expresión coloquial "
            "o ambigua. Conserva el significado y la extensión aproximada del "
            "texto original.\n\n"
            f"ARTÍCULO:\n{texto}"
        )
    else:
        raise ValueError(
            f"Tarea no reconocida: '{tarea}'. Usa 'resumir' o 'profesionalizar'."
        )

    configuration = types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        max_output_tokens=1500,
        temperature=0.3,
    )

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=configuration
    )

    return response.text


if __name__ == "__main__":
    articulo_ejemplo = """
    La inteligencia artificial está cambiando muchísimo cómo trabajamos hoy en día.
    Antes las empresas gastaban un montón de tiempo haciendo tareas repetitivas a mano,
    pero ahora con estas herramientas nuevas las cosas van muchísimo más rápido.
    Igual hay gente que todavía no confía del todo en esto y prefiere hacerlo como
    siempre se ha hecho, lo cual también se entiende porque es un cambio grande.
    """

    print("--- Ejercicio 2: Procesador de Textos Inteligente ---\n")

    print("--- RESUMEN ---\n")
    resumen = procesar_articulo(articulo_ejemplo, "resumir")
    print(resumen)

    print("\n--- PROFESIONAL ---\n")
    profesional = procesar_articulo(articulo_ejemplo, "profesionalizar")
    print(profesional)