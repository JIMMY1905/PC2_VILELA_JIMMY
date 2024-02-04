numero = int(input("Ingrese un número para verificar si es primo: "))
x=1
divisores=0
while x<=numero:
    if numero%x==0:
        divisores = divisores+1
    x=x+1
pass

if divisores==2:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

