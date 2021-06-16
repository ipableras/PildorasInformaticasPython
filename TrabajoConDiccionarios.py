
#Clave:Valor
lasCapitales = {"España":"Madrid", "Francia": "París", "Reino Unido":"Londres"}

print(lasCapitales)

# Añadir una nueva
lasCapitales["Colombia"] = "Bogotá"
print(lasCapitales)

# Cambiar una clave, en este caso con Francia
lasCapitales["Francia"] = "Toulousse"
print(lasCapitales)

# Borrar
del lasCapitales["Reino Unido"]
print(lasCapitales)

############
print()
print()
############

# Tipo dinámico
datos = {"España":"Madrid", 23:"M Jordan", "Mosqueteros":3}
print(datos)

print()
print()

# Listas
claveCapitales=["España", "Reino Unido", "Colombia", "Portugal"] 
print(claveCapitales)

capitalesMundo = {claveCapitales[0]:"Madrid", claveCapitales[1]:"Londres", claveCapitales[2]:"Bogotá"}
print(capitalesMundo)

print(capitalesMundo["Colombia"])

print(capitalesMundo.keys())

print(capitalesMundo.values())

print(len(capitalesMundo))

##############
print()
print()
#############

#Diccionarios con Diccionarios
datosJordan={23:"Jordan", "Nombre":"Michael", "Equipo":"C Bulls", "anillos":[1991, 1992, 1993, 1996, 1997, 1998]}

print(datosJordan)
print(datosJordan["anillos"])

datosJordan={23:"Jordan", "Nombre":"Michael", "Equipo":"C Bulls", "anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}

print(datosJordan.keys())
print(datosJordan)
print(datosJordan["anillos"])


