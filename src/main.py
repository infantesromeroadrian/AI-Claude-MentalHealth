import os
from wellness_assistant import WellnessAssistant

def main():
    with open("secret_key.txt", "r") as file:
        api_key = file.read().strip()

    assistant = WellnessAssistant(api_key)
    print("Bienvenido al Asistente de Bienestar. ¿Cómo puedo ayudarte hoy?")
    while True:  # Este bucle permitirá al usuario hacer múltiples preguntas hasta que decida salir.
        user_input = input("Ingresa tu pregunta o escribe 'salir' para finalizar: ")
        if user_input.lower() == 'salir':  # Si el usuario escribe 'salir', el programa terminará.
            print("Gracias por usar el Asistente de Bienestar. ¡Hasta la próxima!")
            break
        response = assistant.get_response(user_input)
        print(response)

if __name__ == "__main__":
    main()
