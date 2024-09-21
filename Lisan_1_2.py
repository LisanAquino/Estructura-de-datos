def mayor_unico(a, b, c):
    maximo = a 
    contador_maximos = 1 

    if b > maximo:
        maximo = b
        contador_maximos = 1
    elif b == maximo:
        contador_maximos += 1

    if c > maximo:
        maximo = c
        contador_maximos = 1
    elif c == maximo:
        contador_maximos += 1

    return maximo if contador_maximos == 1 else -1

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado = mayor_unico(num1, num2, num3)

if resultado != -1:
    print("El mayor número único es:", resultado)
else:
    print("No existe un mayor número único.")