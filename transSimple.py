"Algoritmo Cryptografico de Transposicion Simple"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys

def cifrarTransSimple(frase):
	cryptograma=''
	lon=len(frase)//2
	if(len(frase)%2!=0):
		lon=lon+1
	for n in range(0,len(frase),2):
		try:
			cryptograma=cryptograma+frase[n]
		except:
			pass	
		
	for n in range(1,len(frase),2):
		try:
			cryptograma=cryptograma+frase[n]
		except:
			pass
	return cryptograma

def desTransSimple(crypto):
	mensaje=""
	lon=len(crypto)//2
	if(len(crypto)%2!=0):
		lon=lon+1
	bloque1=crypto[:lon]
	bloque2=crypto[lon:]
	for n in range(0,lon):
		try:
			mensaje=mensaje+bloque1[n]
			mensaje=mensaje+bloque2[n]
		except:
			pass
	return mensaje

def imprimirAyuda():
	print("transSimple.py es un programa para codificar un archivo usando el algoritmo")
	print("de transposicion simple")
	print(" ")
	print("SINTAXIS:")
	print("python transSimple.py -parametro -e archivo_entrada -s archivo_salida")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python transSimple.py -c -e entrada.txt -s salida.cif                       |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")

if len(sys.argv)<2:
	imprimirAyuda()
elif sys.argv[1]=="-a":
	imprimirAyuda()
else:
	parametro=sys.argv[1]
	inIndex=0
	outIndex=0
	for n in range(0,len(sys.argv)):
		if(sys.argv[n]=="-e"):
			inIndex=n+1
		if(sys.argv[n]=="-s"):
			outIndex=n+1
	try:
		if(inIndex==0):
			raise ValueError
	except ValueError:
		print("No hay archivo de entrada")
	try:
		file=sys.argv[inIndex]
		input1=open(file, "rb")
		size=len(input1.read())
		input1.close()
		input=open(file, "rb")
	except:
		print("No se pudo abrir el archivo de entrada")
		
	if (parametro=="-c"):
		try:
			if outIndex==0:
				file2=file
				if("." in file):
					file2=file[:file.index(".")]
			else:
				file2=sys.argv[outIndex]
			if(not ("." in file2)):
				file2=file2+".cif"
			output=open(file2, "w")
			for n in range(0,size,72):
				output.write(cifrarTransSimple(input.read(72)))
			input.close()
			output.close()
		except:
			print("No se pudo abrir el archivo de salida")
		
	
	elif(parametro=="-d"):
		try:
			if outIndex==0:
				file2=file
				if("." in file):
					file2=file[:file.index(".")]
			else:
				file2=sys.argv[outIndex]
			if(not("." in file2)):
				file2=file2+".dec"
			output=open(file2, "w")
			for n in range(0,size,72):
				output.write(desTransSimple(input.read(72)))
			input.close()
			output.close()
		except:
			print("No se pudo abrir el archivo de salida")
	else:
		imprimirAyuda()
