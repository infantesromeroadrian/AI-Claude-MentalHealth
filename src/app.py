import streamlit as st
from wellness_assistant import WellnessAssistant
import os

# Obtener la clave API desde una variable de entorno
api_key = os.getenv('ANTHROPIC_API_KEY')

if not api_key:
    st.error("Error: No se ha definido la variable de entorno ANTHROPIC_API_KEY.")
    st.stop()

assistant = WellnessAssistant(api_key)

st.title('Asistente de Ayuda Mental')

st.write("""
Bienvenido al Asistente de Ayuda Mental. Estoy aquí para ofrecerte consejos y respuestas sobre bienestar y salud mental.
¿Cómo puedo ayudarte hoy?
""")

# Campo de entrada para la pregunta del usuario
user_input = st.text_input("Escribe tu pregunta aquí:")

# Botón para enviar la pregunta
if st.button('Enviar'):
    if user_input:  # Verificar si el usuario ha escrito algo
        # Obtener y mostrar la respuesta del asistente
        response = assistant.get_response(user_input)
        st.write(response)
    else:
        st.write("Por favor, escribe una pregunta.")

# Opcional: agregar un pie de página o información de contacto
st.markdown("""
---
### ¿Necesitas más ayuda?
Si te sientes abrumado y necesitas hablar con un profesional, no dudes en buscar ayuda. Aquí puedes encontrar algunos recursos: [Línea de Ayuda Nacional](https://example.com).
""")
