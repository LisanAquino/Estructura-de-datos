python_cuatrimestre=12000
python_mensual= python_cuatrimestre / 4
python_descuento= python_mensual * 0.15
python_mensual_con_descuento = python_mensual - python_descuento
nombre= input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))
fecha_de_nacimiento=input("Ingrese fecha de nacimineto: ")
monto_de_matricula= int(input("Ingrese el monto de la matricula: "))
titulosec= True
cuota=(monto_de_matricula + 1000)

print("""======================================================================
=========================== Python Inscripciones =====================
=====================================================================""")
print("DATOS INGRESADOS: ")
print("Nombre ingresado:", nombre)
print(f"Fecha de nacimiento y edad: {fecha_de_nacimiento} ({edad})")
print("Posee titulo?: " , titulosec)
print("Precio matricula: ", monto_de_matricula)
print("Cuota mensual a pagar: ", cuota )
print("Arancel mensual de la materia: ", python_mensual)
print("Arancel mensual de la materia con descuento incluido:", python_mensual_con_descuento)

