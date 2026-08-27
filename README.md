# Taller_Practico
--------------------
# Ejercicio 1: Conexión y Petición Básica
Script básico en Python diseñado para inicializar el cliente oficial de Google GenAI y realizar una consulta directa al modelo de lenguaje. Su propósito principal es validar la conexión correcta con la API y cumplir con la restricción de resumir un concepto técnico en menos de 50 palabras.

- Características Principales
    - Inicialización del Cliente: Conexión directa utilizando la librería moderna google-genai y la clave de API segura.
    - Consulta Específica: Envía un prompt solicitando la definición exacta del concepto "Inferencia en IA".
    - Restricción de Longitud: Configurado para que el modelo entregue una explicación concisa de menos de 50 palabras.
    - Manejo de Variables de Entorno: Integración con python-dotenv para proteger y cargar las credenciales de manera profesional.

- Requisitos Previos
    - Tener instalado Python 3.10 o superior.
    - Una clave de API activa de Google AI Studio.

- Instalación y Configuración
    - Crear y activar un entorno virtual:
    - python -m venv env
    - .\env\Scripts\Activate.ps1

- Instalar las dependencias necesarias:
    - pip install google-genai python-dotenv

- Configurar las credenciales:
    - Crea un archivo llamado .env en la misma carpeta del proyecto y añade tu clave de API:
    - GENAI_API_KEY=tu_clave_de_api_aqui

- Ejecución del Script
    - Ejecuta el script desde tu terminal con el siguiente comando:
    - python ejercicio1.py

------
# Ejercicio 2: Procesador de Textos Inteligente
Script en Python diseñado para procesar y editar artículos utilizando la API oficial de Google GenAI. Cuenta con un rol de Editor Editorial configurado mediante system_instruction para ejecutar tareas de resumen ejecutivo o profesionalización de textos de forma precisa y formal.

- Características Principales
  - Rol Editorial Personalizado: Configura una personalidad exigente y profesional mediante system_instruction que responde de forma directa sin introducciones innecesarias.
  - Manejo de Errores y Logging: Captura excepciones de la API y valida que solo se ingresen tareas reconocidas.
  - Funcionalidad Dual: Permite procesar el texto según la tarea solicitada ("resumir" o "profesionalizar") de forma modular.
  - Configuración Avanzada: Controla la longitud y la creatividad de la respuesta mediante los parámetros max_output_tokens y temperature=0.3.
  - Manejo de Errores y Logging: Captura excepciones de la API y valida que solo se ingresen tareas reconocidas.

- Requisitos Previos
  -  Tener instalado Python 3.10 o superior.
  -  Una clave de API activa de Google AI Studio.

- Instalación y Configuración
  - Crear y activar un entorno virtual:
  - python -m venv env
  - .\env\Scripts\Activate.ps1

- Instalar las dependencias necesarias:
  - pip install google-genai python-dotenv

- Configurar las credenciales:
  - Crea un archivo llamado .env en la misma carpeta del proyecto y añade tu clave de API:
  - GEMINI_API_KEY=tu_clave_de_api_aqui

- Ejecución del Script
  - Ejecuta el script desde tu terminal con el siguiente comando:
  - python ejercicio2.py


----
# Ejercicio 3: Chat de Soporte con Historial (Few-Shot)
Sistema de chat conversacional interactivo para una tienda especializada en maquillaje y belleza, desarrollado en Python con la librería oficial de Google GenAI (google-genai). Utiliza system_instruction para actuar como una asesora de belleza amable y cuenta con historial precargado (Few-shot) con precios en pesos colombianos (COP).

- Características Principales
  - Rol Personalizado: Instrucciones de sistema para definir una personalidad experta en cuidado personal y cosmética.
  - Historial Few-shot: Precarga interacciones previas para establecer el tono y contexto de productos de belleza.
  - Bucle Interactivo: Mantiene la conversación activa hasta que el usuario escribe la palabra clave "finalizar".

- Requisitos e Instalación General
  - Tener instalado Python 3.10 o superior.

- Crear y activar tu entorno virtual:
  - python -m venv env
  - .\env\Scripts\Activate.ps1

- Instalar las dependencias:
  - pip install google-genai python-dotenv

- Configurar tu clave de API en un archivo .env:
  - GENAI_API_KEY=tu_clave_de_api_aqui

- Ejecución
  - python ejercicio3.py
 

