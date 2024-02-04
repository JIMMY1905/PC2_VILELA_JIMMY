numero_ingresado = 15789000
digito = 0
    # Convertir el número a una cadena de texto para utilizar el método count
numero_str = str(numero_ingresado)
    # Contar la cantidad de veces que aparece el dígito en el número
cantidad = numero_str.count(str(digito))
print(f"Número ingresado: {numero_ingresado} y Dígito: {digito}")
print(f"Cantidad de veces {digito} en el número {numero_ingresado}: {cantidad}")
