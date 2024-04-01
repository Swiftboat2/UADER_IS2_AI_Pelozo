import openai

# Configura tu clave de API de OpenAI
openai.api_key = "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"

# Variable global para almacenar la última consulta
ultima_consulta = ""

def obtener_respuesta(input_text):
    try:
        # Invoca la API de chatGPT para obtener una respuesta
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": input_text}],
            max_tokens=50,
            temperature=0.7
        )
        return response.choices[0].message['content']
    except Exception as e:
        print("Error al obtener respuesta de chatGPT:", e)
        return None

def main():
    global ultima_consulta  # Declarar que la variable global será modificada dentro de esta función

    while True:
        try:
            # Acepta una consulta del usuario
            consulta = input("You: ")

            # Verifica si la consulta tiene texto
            if consulta.strip():
                try:
                    # Imprime la consulta del usuario
                    print("You:", consulta)

                    # Almacena la consulta como la última consulta realizada
                    ultima_consulta = consulta

                    # Invoca la API de chatGPT con la consulta del usuario
                    respuesta = obtener_respuesta(consulta)

                    if respuesta is not None:
                        # Imprime la respuesta de chatGPT
                        print("chatGPT:", respuesta)
                    else:
                        print("No se pudo obtener una respuesta.")
                except Exception as e:
                    print("Error en el tratamiento de la consulta:", e)
            else:
                print("Por favor ingresa una consulta válida.")
        except KeyboardInterrupt:
            print("\n¡Adiós!")
            break

        # Manejar la edición de la última consulta con la tecla "cursor Up"
        try:
            consulta_editada = input("You (Editar, Enter para enviar): " + ultima_consulta)
            if consulta_editada.strip():
                ultima_consulta = consulta_editada
        except KeyboardInterrupt:
            print("\n¡Adiós!")
            break

if __name__ == "__main__":
    main()
