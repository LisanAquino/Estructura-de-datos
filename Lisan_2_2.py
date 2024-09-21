def es_fecha_valida(dia, mes, año):
  if dia <= 0 or mes <= 0 or año <= 0:
    return False

  if mes > 12:
    return False

  dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    dias_por_mes[1] = 29
  if dia > dias_por_mes[mes - 1]:
    return False

  return True
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

if es_fecha_valida(dia, mes, año):
  print("La fecha es válida.")
else:
  print("La fecha no es válida.")  
