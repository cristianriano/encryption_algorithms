# -*- coding: utf-8 -*-
"Algoritmo Cryptografico Vigenere"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys
import hashlib

def cifrar(cripto, k):
	mensaje=""
	while(len(cripto)>0):
		for n in range(len(k)):	
			try:
				if(ord(cripto[n])==209): mensaje=mensaje+posicionLetras[(14+k[n])%alfabeto]
				else: mensaje=mensaje+posicionLetras[(letrasPosicion[cripto[n]]+k[n])%alfabeto]
			except:
				try:
					mensaje=mensaje+cripto[n]
				except:
					pass
		cripto=cripto[len(k):]
	return mensaje

def decifrar(cripto, k):
	mensaje=""
	while(len(cripto)>0):
		for n in range(len(k)):	
			try:
				mensaje=mensaje+posicionLetras[(letrasPosicion[cripto[n]]-k[n])%alfabeto]
			except:
				try:
					mensaje=mensaje+cripto[n]
				except:
					pass
		cripto=cripto[len(k):]
	return mensaje

#Lee un archivo y retorna su hash en hexadecimal
def hashArchivo(archivo,metodo,bloque=1000):
	buf = archivo.read(bloque)
	while(buf!=""):
		metodo.update(buf)
		buf = archivo.read(bloque)
	return metodo.hexdigest()

def imprimirAyuda():
	print("vigenere.py es un programa para cifrar un archivo usando el algoritmo de vigenere")
	print("usando una clave")
	print(" ")
	print("SINTAXIS:")
	print("python vigenere.py -cifrado_decifrado -e archivo_entrada -s archivo_salida -k archivo_clave")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|-k      Define el archivo donde esta la clave                               |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python vigenere.py -c -e entrada.txt -s salida.cif -k clave.txt             |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("23-Octubre-2014")

letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", u'Ñ', "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
alfabeto=28
lineas=10

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
	claveIndex=0
	#Se obtienen los argumentos ingresados por el shell
	for n in range(0,len(sys.argv)):
		if(sys.argv[n]=="-e"):
			inIndex=n+1
		if(sys.argv[n]=="-s"):
			outIndex=n+1
		if(sys.argv[n]=="-k"):
			claveIndex=n+1
	flag=False
	try:
		if(inIndex==0):
			raise NameError
		if(claveIndex==0):
			raise ZeroDivisionError
		file=sys.argv[inIndex]
		input=open(file, "rb")
		fileClave=sys.argv[claveIndex]
		inputClave=open(fileClave, "rb")
		k=inputClave.read().decode("utf-8")
		clave=[]
		for n in k:
			clave.append(n)
		for n in clave:
			if(not(n in letras)):
				clave.remove(n)
		for n in range(len(clave)):
			clave[n]=letrasPosicion[clave[n]]
		longitud=len(clave)
		flag=True
	except ZeroDivisionError:
		print("No hay archivo de clave")
		imprimirAyuda()
	except NameError:
		print("No hay archivo de entrada")
		imprimirAyuda()
	except:
		print("No se pudo abrir el archivo de entrada")	
	if (parametro=="-c" and flag):
	#	try:
			if outIndex==0:
				file2=file+".cif"
			else:
				file2=sys.argv[outIndex]
			print("     Cifrando archivo....")
			#Se crea un archivo temporal donde esta el archivo codificado
			encode=True
			
			try: 
				p=input.read().decode("utf-8")
				input.seek(0)				
				p=input.read(lineas*longitud).decode("utf-8")
			except: 
				input.seek(0)
				encode=False
				p=input.read(lineas*longitud)
			output=open(file2, "w")
			if(encode):
				while(p!=""):
					output.write(cifrar(p, clave).encode("utf-8"))
					p=input.read(lineas*longitud).decode("utf-8")
			else:
				while(p!=""):
					output.write(cifrar(p, clave).encode("utf-8"))
					p=input.read(lineas*longitud)
			input.close()
			output.close()
			print("     Archivo cifrado!")
			md5=open(file+".MD5","w")
			md5.write(file+": ")
			md5.write(hashArchivo(open(file,"rb"),hashlib.md5()))
			md5.write("\n"+file2+": ")
			md5.write(hashArchivo(open(file2,"rb"),hashlib.md5()))
			md5.close()
	#	except:
	#		print("No se pudo abrir el archivo de salida")
		
	
	elif(parametro=="-d" and flag):
		try:
			if outIndex==0:
				file2=file+".dec"
			else:
				file2=sys.argv[outIndex]
			output=open(file2,"w")
			print("     Decifrando archivo....")
			p=input.read(lineas*longitud).decode("utf-8")
			output=open(file2, "w")
			while(p!=""):
				output.write(decifrar(p, clave).encode("utf-8"))
				p=input.read(lineas*longitud).decode("utf-8")
			input.close()
			output.close()
			print("     Archivo decifrado!")
			md5=open(file+".MD5","w")
			md5.write(file+": ")
			md5.write(hashArchivo(open(file,"rb"),hashlib.md5()))
			md5.write("\n"+file2+": ")
			md5.write(hashArchivo(open(file2,"rb"),hashlib.md5()))
			md5.close()
		except:
			print("No se pudo abrir el archivo de salida")
	elif(flag):		
		imprimirAyuda()
