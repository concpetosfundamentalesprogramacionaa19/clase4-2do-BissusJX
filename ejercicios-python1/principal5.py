"""
    @reroes
    Manejo de estructuras
"""

diccionario = {"nombre": "Diana", "apellidos": "Serrano"}
diccionario2 = {"nombre": "René", "apellidos": "Elizalde"}

lista = [diccionario,diccionario2]
print("Imprimir diccionario")
for l in lista:
	midiccionario = l
	print("Mi nombre es: %s y mi apellido es: %s"% \
			(midiccionario["nombre"], \
				midiccionario["apellidos"]))



