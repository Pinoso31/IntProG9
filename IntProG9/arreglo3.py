print("Lista principal desordenada")
edades = [17, 16, 18, 20, 14, 21, 27]
print(edades)

#ordenar de menor a mayor 
print("Lista dada ordenada de menor a mayor")
edades.sort()
print(edades)

#ordenar de mayor a menor 
print("Lista dada ordenada de mayor a menor")
edades.sort(reverse=True)
print(edades)

import statistics as st

#mostrar la media 
media = st.mean(edades)
print(f"Media : {media}")

#mostrar la moda 
moda = st.mode(edades)
print(f"Moda: {moda}")

#st.mean es la media de edades que mas hay
#st.mode es lo que mas se repite