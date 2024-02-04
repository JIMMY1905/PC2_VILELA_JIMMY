texto_usuario = input("Ingrese una cadena de texto: ")
vocales = "AEIOUaeiou"
resultado = ""
for char in texto_usuario:
    if char not in vocales:
        resultado = resultado + char
print("Texto con vocales omitidas:", resultado)


