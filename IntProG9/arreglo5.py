#leer x cantidad de numeros y decir cuantos son pares y cuantos son impares
sumas_pares = 0
suma_impares = 0
numeros = []

while True:
    numero = int(input("Dime un numero : "))
    numeros.append(numero)

    resp = input("Desea agregar otro? [S] si o [N] no: ")
    if resp.upper() == "N":
        False
        break

cont = 0
while True:
    for numero in numeros:
        if numero %2 == 0:
            suma_pares += 1
        elif numero % 2 !=0:
            suma_impares += 1

    print(f"Suma de pares: {suma_pares}")
    print(f"Suma de impares: {suma_impares}")