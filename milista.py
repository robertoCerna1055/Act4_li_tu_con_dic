# Ejemplos de uso de listas 

Misnovias = ["Agripina", "Anastacia", "Maria"]
misNumeros = [666, 77, 10]

# Mostrando mis novias
print("")
print(Misnovias)

# Mostrando mis numeros
print(misNumeros)
print("")

print("----Accediendo a los elementos de la lista----")

print(Misnovias[1])
if "Agripina" in Misnovias:
  print("Si, 'Agripina' esta en la lista de mis novias")
else:
  print("Chale")

Nnovias = len(Misnovias)
print(f"Numero de novias: {Nnovias}")

print("Ciclo for en listas")
posicion = 0
for medianaranja in Misnovias:
  print(posicion,"    ",medianaranja)
  posicion = posicion + 1
