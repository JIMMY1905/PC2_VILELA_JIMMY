# Ingreso de datos de los alumnos
n = int(input("Ingrese el número de alumnos: "))
alumnos = []

for _ in range(n):
    #repetimos el bucle n veces
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []

    for i in range(3):
            nota = float(input(f"Ingrese la nota {i + 1} del alumno {nombre}: "))
            notas.append(nota)
            alumno={"Alumno":nombre,"Notas":notas}
 ##Acabamos de llenar el formato del primer alumno y lo añadimos a la lista de Alumnos, y seguimos con el siguiente Alumno
            alumnos.append(alumno)
    pass    
    ##Ahora mostramos los datos de todos los alumnos
    print("\nListado completo de alumnos:")
    for alumno in alumnos:
      print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

