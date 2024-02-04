limite = 50
fib_series = [0, 1]
while fib_series[-1] + fib_series[-2] <= limite:
        ##verificamos que la suma de los dos últimos términos nos de 50 para parar la serie 
        fib_series.append(fib_series[-1] + fib_series[-2])
##añadimos como elemento nuevo a la suma de los dos últimos números de la serie o lista
print(f"Serie de Fibonacci hasta {limite}:")
print(fib_series)
