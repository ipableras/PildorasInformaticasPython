# Tuplas
# Son mas rapidas, pero son más rigidas

misDatos = ("Juan", 13, 1, 2002)

print(misDatos)

misDatosLista=list(misDatos)
print(misDatosLista)

# Vamos a hacerlo alreves
misDatos2 = ["Juan", 13, 1, 2002]

misDatosTupla = tuple(misDatos2)
print(misDatosTupla)

print()

# De esta forma otra vez
misDatosTupla = list(misDatos2)
print(misDatosTupla)
misDatosTupla = tuple(misDatos2)
print(misDatosTupla)

print()

# Vamos a ver que estamos mirando en la Tupla
print(13 in misDatosTupla)
print(25 in misDatosTupla)
print("Juan" in misDatosTupla)

print()

# count()
print(misDatosTupla.count("Juan"))
print(misDatosTupla.count("Jua"))
print(misDatosTupla.count(13))
misDatosTupla = ("Juan", 13, 1, 2002, "Juan")
print(misDatosTupla)
# Ahora tenemos dos numeros en "Juan"
print(misDatosTupla.count("Juan"))

print()

# len()
print(len(misDatosTupla))

print()

# desempaquetado de tupla
print(misDatos)
nombre, dia, mes, agno=misDatos
print(mes)

# desempaquetado de tupla 2
# Es decir, los nombres me los invento yo
print(misDatos)
nom, d, m, agn=misDatos
print(m)
