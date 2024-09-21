print("======================= Aulas ========================")
dia = int(input("Ingrese el número del día: 1 (lunes) a 6 (sábado): "))

if dia < 1 or dia > 6:
    print("Número de día inválido. Debe estar entre 1 y 6.")
else:
    if dia % 2 == 0:  # Si es par
        aula = "A-300"
    else:  # Si es impar
        aula = "A-315"
    
    print(f"Aula: {aula}")
print("\n=============== Descuentos y estacionamiento ===============")
turno = input("Ingrese el turno: Mañana, Tarde o Noche: ").capitalize() 
materias = int(input("Ingrese la cantidad de materias: "))
cuota = float(input("El valor de la cuota es: "))
if turno == "Tarde" and materias > 3:
    descuento = 0.25  
else:
    descuento = 0.05  
cuota_con_descuento = cuota * (1 - descuento)
print(f"El valor de la cuota con descuento es: {cuota_con_descuento:.1f}")

vehiculo = input("Ingrese el vehículo en el que ingresa: Auto, Moto o Bicicleta: ").capitalize()
if vehiculo == "Auto" or vehiculo == "Moto":
    costo_estacionamiento = 300
elif vehiculo == "Bicicleta":
    costo_estacionamiento = 50
else:
    costo_estacionamiento = 0
    print("Opción de vehículo inválida. No se asignará costo de estacionamiento.")
if costo_estacionamiento > 0:
    print(f"El costo de estacionamiento para {vehiculo} es: {costo_estacionamiento}")
