sabores = ["chocolate", "creama americana", "vainilla", True, 10,12.5]  #Variable de variables (analogía)
print(sabores)
print(type(sabores))

for x in sabores:
    print(type(x))

sabor = "fresa"
print(sabor.upper())

print(sabores.pop(1))
print(sabores)
sabores.append(sabor) #Agrega elemento al final de la lista
print(sabores)

sabores.insert(2, "nuevo elemento") #inserta un elemento en la posicion indicada, el emento anterior se corre a la derecha
print(sabores)

sabores2 = ["dulce de leche", "azucarada"]
sabores.extend(sabores2) #Adozar la lista completa a otra lista al final de si misma
print(sabores)

sabores.remove(True) #Elimina la primera aparición del valor
print(sabores)
