aulas = {
    1: "A-315",
    2: "A-305",
    3: "A-315",
    4: "A-315",
    5: "A-315",
    6: "A-300"
}

print("============ Listado de aulas ============")
print("{:<5} {:<10}".format("Día", "Aula"))
for dia, aula in aulas.items():
    print("{:<5} {:<10}".format(dia, aula))
intentos = 0
edad_valida = False

print("============ Carga de edades ============")

while not edad_valida:
    edad = int(input("Ingrese una edad mayor o igual a 18: "))

    if edad >= 18:
        edad_valida = True 
        print(f"Edad válida ingresada: {edad}")
    else:
        intentos += 1 
        print(f"Error! Ingrese una edad mayor o igual a 18. Se ha ingresado la edad erróneamente {intentos} veces.")

notas = []
print("============ Promedio de notas ============")

for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio:.1f}")

cuota_diaria = 1250
print("============ Costo del comedor ============")
print("{:<5} {:<10}".format("Día", "Costo"))
for dia in range(1, 7):
    costo_total = cuota_diaria * dia
    print("{:<5} ${:<10}".format(dia, costo_total))