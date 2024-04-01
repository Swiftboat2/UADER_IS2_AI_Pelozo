import openai

openai.api_key = "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"

def main():
    try:
        # Solicita la consulta al usuario
        try:
            query = input("Ingrese su consulta: ")
            if not query.strip():
                print("La consulta está vacía.")
                return
        except Exception as input_error:
            print("Error al solicitar la consulta:", input_error)
            return

        # Imprime la consulta del usuario
        print("You:", query)

        # Invoca el modelo de ChatGPT con la consulta del usuario
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",  # Updated model
                messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}],
                max_tokens=50,
                temperature=0.7
            )
        except Exception as api_error:
            print("Error al invocar el modelo de ChatGPT:", api_error)
            return

        # Imprime la respuesta de ChatGPT
        try:
            print("chatGPT:", response.choices[0].message['content'].strip())
        except Exception as response_error:
            print("Error al obtener la respuesta de ChatGPT:", response_error)

    except Exception as e:
        print("Error general:", e)

if __name__ == "__main__":
    main()
