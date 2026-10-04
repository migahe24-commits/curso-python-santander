#Pide al usuario una operación (suma, resta, multiplicación, división) y dos números.
#Ejecute la operación y muestre el resultado.
#Debe repetirse hasta que el usuario escriba "salir" como operación.

#Sugerirte cómo estructurar el loop principal.
#Generar la lógica de cada operación (quizá usar un diccionario de funciones o if/elif).
#Manejar división por cero (puedes pedirle a la IA cómo).
#Probar distintos inputs.

while True:
    operacion = input("Introduce la operación (suma, resta, multiplicacion, division) o 'salir' para terminar: ")
    if operacion == "salir":
        break
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if operacion == "suma":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacion == "resta":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacion == "multiplicacion":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operacion == "division":
        if num2 == 0:
            print("Error: No se puede dividir por cero")
            continue
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Operación no válida")
  
