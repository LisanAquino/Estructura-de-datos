dinero_recibido = int(input("Ingrese cantidad de dinero recibido: "))

total_compra = int(input("Ingrese total de la compra: "))

if dinero_recibido < total_compra :
 print("Dinero insuficiente")

cambio = dinero_recibido - total_compra
billetes = [500, 100, 50, 20, 10, 5, 1]
cantidad_billetes = {}

for billete in billetes:
    cantidad_billetes[billete] = cambio // billete
    cambio %= billete

print("billtes"), cantidad_billetes


resultado = calcular_cambio(total_compra, dinero_recibido)

if isinstance(resultado, str):
  print(resultado)
else:
  for billete, cantidad in resultado.items():
    print(f"Billetes de ${billete}: {cantidad}")