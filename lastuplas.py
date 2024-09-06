arcoiris = ("Azul","Verde","Rojo","Amarillo")
print(arcoiris)

print("-- Longitud del arcoiris --")
print(len(arcoiris))

animales = ("Pantera", 20, "Estatura", 1.7)
print(animales)

print("Elementos de la tupla")
print(animales[1])

rateros  = ("Juan", "Ana", "Pedro")
y = list(rateros)
y[1] = "Polainas"
x = tuple(y)
print(x)

print("")
print("Agregamos elementos")

Nanimal = ("Boby", "Chetos")
y = list(Nanimal)
print(y)
y.append("Tontolin")
otratupla = tuple(y)
print(otratupla)

print("")
print("Uso de For en tuplas")
for elcolor in arcoiris:
    print(elcolor)