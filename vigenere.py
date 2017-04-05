"Algoritmo Cryptografico Vigenere"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys
import base64
import os
import hashlib

def cifrar(frase, clave):
	cryptograma=''
	for n in range(longitud):
		try:
			#Se calcula el indice del caracter cifrado
				i=((base.index(frase[n]))+(base.index(clave[n])))%alfabeto
				cryptograma=cryptograma+base[i]	
		except:
			pass
	return cryptograma

def descifrar(crypto, clave):
	mensaje=""
	for n in range(longitud):
		try:
			#Se calcula indice de decifrado (formula del algoritmo)
			i=((base.index(crypto[n]))-(base.index(clave[n])))%alfabeto
			mensaje=mensaje+base[i]
		except:
			pass
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

base=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]
alfabeto=64

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
		k=inputClave.read()
		clave=[]
		k=base64.b64encode(k)
		for n in k:
			clave.append(n)
		#En caso que la codificacion de la clave tenga = se quitan
		for n in clave:
			if(not(n in base)):
				clave.remove(n)
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
		try:
			if outIndex==0:
				file2=file
				if("." in file):
					file2=file[:file.index(".")]
			else:
				file2=sys.argv[outIndex]
			if(not ("." in file2)):
				file2=file2+".cif"
			tmp=open(file+".tmp","w")
			print("     Cifrando archivo....")
			#Se crea un archivo temporal donde esta el archivo codificado
			p=input.read(600)
			while(p!=""):
				tmp.write(base64.b64encode(p))
				p=input.read(600)
			tmp.close()
			input.close()
			tmp=open(file+".tmp","rb")
			p=tmp.read(longitud)
			output=open(file2, "w")
			while(p!=""):
				output.write(cifrar(p, clave))
				p=tmp.read(longitud)
			tmp.close()
			output.close()
			os.remove(file+".tmp")
			print("     Archivo cifrado!")
			md5=open(file+".MD5","w")
			md5.write(file+": ")
			md5.write(hashArchivo(open(file,"rb"),hashlib.md5()))
			md5.write("\n"+file2+": ")
			md5.write(hashArchivo(open(file2,"rb"),hashlib.md5()))
			md5.close()
		except:
			print("No se pudo abrir el archivo de salida")
		
	
	elif(parametro=="-d" and flag):
		try:
			if outIndex==0:
				file2=file
				if(file2[-4:]==".cif"):
					file2=file2[:-4]+".dec"
				else:
					file2=file2+".dec"
			else:
				file2=sys.argv[outIndex]
			tmp=open(file+".tmp","w")
			print("     Decifrando archivo....")
			p=input.read(longitud)
			while(p!=""):
				tmp.write(descifrar(p, clave))
				p=input.read(longitud)
			tmp.close()
			input.close()
			tmp=open(file+".tmp","r+")
			tmp.read()
			lon2=tmp.tell()
			if(lon2%4==3):
				tmp.write("=")
			elif(lon2%4==2):	
				tmp.write("==")
			tmp.seek(0)
			p=tmp.read(600)
			output=open(file2, "w")
			while(p!=""):
				output.write(base64.b64decode(p))
				p=tmp.read(600)
			tmp.close()
			output.close()
			os.remove(file+".tmp")
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
