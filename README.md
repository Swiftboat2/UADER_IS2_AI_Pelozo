# pylint errores

Line too long (127/100):

Decidí no abordar esta recomendación porque la longitud de la línea no excede significativamente el límite de 100 caracteres. Además, acortar la línea podría comprometer la legibilidad o claridad del código, ya que no es una violación grave del límite de longitud de línea.
Missing module docstring:

Opté por no abordar esta recomendación porque parece ser una omisión menor y el propósito y la funcionalidad del módulo ya están claramente definidos en los comentarios inmediatamente antes del código. Aunque agregar una cadena de documento del módulo sería una buena práctica, su ausencia no afecta la funcionalidad ni la comprensión del código en este caso.
Catching too general exception Exception (broad-exception-caught):

Decidí no abordar esta recomendación porque mantener una cláusula except Exception al final del bloque de manejo de excepciones puede ser útil para atrapar cualquier excepción no esperada que pueda ocurrir. Esto puede ayudar a identificar y manejar problemas no previstos de manera más robusta y proporcionar información de depuración útil en caso de fallo del programa.
Using the global statement (global-statement):

Opté por no abordar esta recomendación porque el uso del global statement es necesario en este caso para modificar la variable global LAST_QUERY dentro de la función main(). Aunque su uso puede hacer que el código sea menos modular y más difícil de depurar, en este caso particular, es necesario para mantener el estado del programa entre iteraciones del bucle principal.