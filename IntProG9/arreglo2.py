estudiantes = ["Jorge Picado", "Franklin Callejas", "Josue espinoza", "Joshua Saencz"]

tamaño = len(estudiantes)

print(f"\nCantidad de estudiantes : {tamaño}")

#recorrer los elementos del arreglo
for estudiante in estudiantes:
    print(f"{estudiante} tiene {len(estudiante)} letras")
    
    #para imprimir las vocales
    vocales = "aeiou"
    sumavoc = 0
    for letra in estudiante:
        if letra in vocales:
            sumavoc += 1
        print(f"{letra.upper()} "*1)
    print(f"{estudiante} tiene {sumavoc} vocales")
    
