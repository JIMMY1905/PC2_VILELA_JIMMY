
numero = int(input("Ingrese un número para calcular su factorial: "))
if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0 or numero == 1:
    print(f"El factorial de {numero} es: 1")
else:
    resultado = 1
    while numero > 1:
        resultado = resultado* numero
        numero = numero- 1
    print(f"El factorial es: {resultado}")
