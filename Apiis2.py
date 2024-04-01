import openai

openai.api_key = "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"

def main():
    # Solicita la consulta al usuario
    query = input("Ingrese su consulta: ")

    # Verifica si la consulta tiene texto
    if query.strip() == "":
        print("La consulta está vacía.")
        return

    # Imprime la consulta del usuario
    print("You:", query)

    # Invoca el modelo de ChatGPT con la consulta del usuario
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",  # Updated model
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}],
        max_tokens=50,
        temperature=0.7
    )

    # Imprime la respuesta de ChatGPT
    print("chatGPT:", response.choices[0].message['content'].strip())

if __name__ == "__main__":
    main()
