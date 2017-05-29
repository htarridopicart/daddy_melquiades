'''
Algoritmo para crear los mil y mas hits de Daddy Melquiades
por .http.

This work is licensed under the Creative Commons Attribution 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or 
send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA

'''

lista_01 = ["Mami", "Bebe", "Princess", "Maaamiii"]
lista_02 = ["yo quiero", "yo puedo", "yo vengo a", "voy a"]
lista_03 = ["encendelte", "amalte", "ligal", "jugal"]
lista_04 = ["suave", "lento", "rapido", "fuelte"]
lista_05 = ["hasta que salga el sol", "toda la noche", "hasta el amanecel", "todo el dia" ]
lista_06 = ["sin anestesia", "sin compromiso", "feis to feis", "sin miedo"]

regueton_hits = []

regueton_matrix = {}

for item_01 in lista_01:
	for item_02 in lista_02:
		for item_03 in lista_03:
			for item_04 in lista_04:
				for item_05 in lista_05:
					for item_06 in lista_06:
						regueton_hits.append(item_01 + " " + item_02+" "+item_03+" "+item_04+" "+item_05+" "+item_06)
						#regueton_matrix = item_01, item_02, item_03, item
						
cantidad_hits = len(regueton_hits)

print cantidad_hits
						
with open(r'C:\Users\User\Downloads\regueton_hits.txt', 'w') as file:
	print("Espera... Que sstamos escribiendo  los hits del verano!")
	print("\n")
	
	
	
	file.write("Cuatro Mil Canciones Hits del Verano")
	file.write("\n")
	file.write("por Daddy Melquiades")
	file.write("\n")
	
	
	file.write("\n")
	file.write("Cantidad de hits del verano: " + str(cantidad_hits))
	file.write("\n")
	
	
	file.write("\n")
	file.write("\n")
	file.write("La lista y sus permutaciones: ")
	file.write("\n")
	file.write("\n")
	
	#la tabla de daddy melquiades
	i = 0
	
	while  i < len(lista_01):
		file.write(lista_01[i])
		file.write(" ")
		file.write(" | ")
		file.write(lista_02[i])
		file.write(" ")
		file.write(" | ")
		file.write(lista_03[i])
		file.write(" ")
		file.write(" | ")
		file.write(lista_04[i])
		file.write(" ")
		file.write(" | ")
		file.write(lista_05[i])
		file.write(" ")
		file.write(" | ")
		file.write(lista_06[i])
		
		file.write("\n")
		i += 1
	
	file.write("\n")
	
	
	#ahora todas la permutaciones
	
	for item in regueton_hits:
		item_index = regueton_hits.index(item) + 1
		
		write_line = str(item_index) + ". " + item
		
		print write_line
		
		file.write(write_line)
		file.write("\n")
	
	file.close()

print("Ya... acabamos! ~ Daddy Melquiades")
print("\n")
