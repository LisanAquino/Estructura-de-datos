nota1 = float(input("Ingrese la nota del primer parcial: "))
nota2 = float(input("Ingrese la nota del segundo parcial: "))

promedio = (nota1 + nota2) / 2

print(f"\nEl promedio de las notas es: {promedio:.1f}")

if nota2 >= 7:
    print("Aprobó el segundo parcial")
else:
    print("Desaprobó el segundo parcial")

if nota2 > nota1:
    print("Progreso del 1er al 2do parcial: Mejoró su desempeño")
elif nota2 == nota1:
    print("Progreso del 1er al 2do parcial: Mantuvo la nota")
else:
    print("Progreso del 1er al 2do parcial: Empeoró su desempeño")

if promedio >= 7:
    print("Promocionó la materia")
elif promedio >= 4:
    print("Debe rendir el final")
else:
    print("Debe recursar la materia")
