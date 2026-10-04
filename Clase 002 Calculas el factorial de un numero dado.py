# Calcular el factorial de un número dado por el usuario
def factorial(n):
    if n == 0 or n == 1:
        return 1  # caso base
    return n * factorial(n - 1)  # caso recursivo
# Solicitar al usuario ingresar un número   
numero = int(input("Ingresa un número: "))
# Calcular el factorial del número ingresado
print(f"El factorial de {numero} es {factorial(numero)}")
# Imprimir el resultado