numeros = []
##declaramos una lista con valores indefinidos
while True:
    ##Usamos While true para que constantemente evalúe si quiere ingresar un número
    decision = input("¿Desea ingresar un número? (SI/NO): ").upper()
    ##usamos UPPER para no tener errores con SI y NO
    if decision == "SI":
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
    elif decision == "NO":
        break
    else:
        print("Ingrese SI o NO")
print("Números ingresados:", numeros)

numeros_pares = sum(1 for num in numeros if num % 2 == 0)
##Sumamos 1's cada vez que encuentre un número par en la lista 'numeros'
numeros_impares = len(numeros) - numeros_pares

print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)
