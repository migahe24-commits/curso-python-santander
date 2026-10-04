#Crear una lista con los cuadrados de los n primeros numeros naturales
n = int(input("Ingrese el numero de terminos: "))
cuadrados = []
for i in range(1, n+1):
    cuadrados.append(i**2)
print(cuadrados)
