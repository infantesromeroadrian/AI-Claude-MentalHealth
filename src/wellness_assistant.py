import logging
import anthropic

class WellnessAssistant:
    def __init__(self, api_key):
        self.client = anthropic.Anthropic(api_key=api_key)

    def get_response(self, user_input):
        try:
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1024,
                messages=[{"role": "user", "content": user_input}]
            )
            if response.content:  # 'content' debería ser accesible directamente si es un atributo
                texts = [block.text for block in response.content if hasattr(block, 'text')]
                return ' '.join(texts) if texts else "La respuesta no contiene texto."
            else:
                return "La respuesta no contiene texto."
        except Exception as e:
            logging.error(f"Se produjo un error al obtener la respuesta: {e}")
            return "Lo siento, se produjo un error al procesar tu solicitud."
