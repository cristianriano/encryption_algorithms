# -*- coding: utf-8 -*-
"Algoritmo Cryptografico de Transposicion por Grupos"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys
import base64

def cifrar(cripto, k):
	mensaje=""
	for n in cripto:
		try:
			mensaje=mensaje+posicionLetras[(letrasPosicion[n]+k)%alfabeto]	
		except:
			mensaje=mensaje+n
	return mensaje

def decifrar(cripto, k):
	mensaje=""
	for n in cripto:
		try:
			mensaje=mensaje+posicionLetras[(letrasPosicion[n]-k)%alfabeto]	
		except:
			mensaje=mensaje+n
	return mensaje

	
def imprimirAyuda():
	print("julio.py es un programa para cifrar un archivo usando el algoritmo de")
	print("sustitucion monoalfabetica de Julio Cesar")
	print(" ")
	print("SINTAXIS:")
	print("python julio.py -cifrado_decifrado -k clave -e archivo_entrada -s archivo_salida")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|-k      Clave                                                               |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python julio.py -c -e entrada.txt -s salida.cif -k 4                     |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("18-Septiembre-2014")

letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
alfabeto=28
lineas=100

letrasPosicion={}
for n in range(alfabeto):
	letrasPosicion[letras[n]]=n

k=letrasPosicion.keys()
posicionLetras={}

for n in k:
	posicionLetras[letrasPosicion[n]]=n

if len(sys.argv)<2:
	imprimirAyuda()
elif sys.argv[1]=="-a":
	imprimirAyuda()
else:
	parametro=sys.argv[1]
	inIndex=0
	outIndex=0
	kIndex=0
	let=False
	for n in range(0,len(sys.argv)):
		if(sys.argv[n]=="-e"):
			inIndex=n+1
		if(sys.argv[n]=="-s"):
			outIndex=n+1
		if(sys.argv[n]=="-k"):
			kIndex=n+1
	flag=False
	try:
		if(inIndex==0):
			raise ValueError
		if(kIndex==0):	
			raise TypeError
		file=sys.argv[inIndex]
		input=open(file, "rb")
		clave=letrasPosicion[(sys.argv[kIndex])]
		flag=True
	except ValueError:
		print("No hay archivo de entrada")
		imprimirAyuda()
	except TypeError:
		print("No hay clave")
		imprimirAyuda()
	except:
		print("No se pudo abrir el archivo de entrada")	
	if (parametro=="-c" and flag):
		try:
			if outIndex==0:
				file2=file+".cif"
			else:
				file2=sys.argv[outIndex]
			output=open(file2, "w")
			p=input.read(72)
			print("     Cifrando archivo....")
			while(p!=""):
				output.write(cifrar(p, clave))
				p=input.read(72)
			input.close()
			output.close()
			print("     Archivo cifrado!")
		except:
			print("No se pudo abrir el archivo de salida")
		
	
	elif(parametro=="-d" and flag):
		try:
			if outIndex==0:
				file2=file+".dec"
			else:
				file2=sys.argv[outIndex]
			output=open(file2, "w")
			p=input.read(72)
			print("     Decifrando archivo....")
			while(p!=""):
				output.write(descifrar(p, clave))
				p=input.read(72)
			input.close()
			output.close()
			print("     Archivo decifrado!")
		except:
			print("No se pudo abrir el archivo de salida")
	elif(flag):		
		imprimirAyuda()
