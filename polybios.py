"Algoritmo Cryptografico de Transposicion por Grupos"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys
import base64

def cifrar(frase, d):
	cryptograma=''
	for n in frase:
		try:
			cryptograma=cryptograma+d[n]
		except: 	
			cryptograma=cryptograma+n
	return cryptograma

def descifrar(crypto, d):
	mensaje=""
	for n in range(0,len(crypto),2):
		try:
			mensaje=mensaje+d[crypto[n:n+2]]
		except:
			mensaje=mensaje+crypto[n:n+2]
	return mensaje

	
def imprimirAyuda():
	print("polybios.py es un programa para cifrar un archivo usando el algoritmo de")
	print("sustitucion monoalfabetica de polybios, usando una matriz de numeros o letras")
	print(" ")
	print("SINTAXIS:")
	print("python polybios.py -cifrado_decifrado -tipo_matriz -e archivo_entrada -s archivo_salida")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|-n      Usar la matriz numerica para el proceso (por defecto)               |")
	print("|-l      Usar la matriz de letras para el proceso                            |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python polybios.py -c -n -e entrada.txt -s salida.cif                       |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("18-Septiembre-2014")
diccionarioN={"A": "11", "B": "12", "C": "13", "D": "14", "E": "15", "F": "16", "G": "17", "H": "18", "I": "21", "J": "22", "K": "23", "L": "24", "M": "25", "N": "26", "O": "27", "P": "28", "Q": "31", "R": "32", "S": "33", "T": "34", "U": "35", "V": "36", "W": "37", "X": "38", "Y": "41", "Z": "42", "a": "43", "b": "44", "c": "45", "d": "46", "e": "47", "f": "48", "g": "51", "h": "52", "i": "53", "j": "54", "k": "55", "l": "56", "m": "57", "n": "58", "o": "61", "p": "62", "q": "63", "r": "64", "s": "65", "t": "66", "u": "67", "v": "68", "w": "71", "x": "72", "y": "73", "z": "74", "0": "75", "1": "76", "2": "77", "3": "78", "4": "81", "5": "82", "6": "83", "7": "84", "8": "85", "9": "86", "+": "87", "/": "88"}

diccionarioL={"A": "AA", "B": "AB", "C": "AC", "D": "AD", "E": "AE", "F": "AF", "G": "AG", "H": "AH", "I": "BA", "J": "BB", "K": "BC", "L": "BD", "M": "BE", "N": "BF", "O": "BG", "P": "BH", "Q": "CA", "R": "CB", "S": "CC", "T": "CD", "U": "CE", "V": "CF", "W": "CG", "X": "CH", "Y": "DA", "Z": "DB", "a": "DC", "b": "DD", "c": "DE", "d": "DF", "e": "DG", "f": "DH", "g": "EA", "h": "EB", "i": "EC", "j": "ED", "k": "EE", "l": "EF", "m": "EG", "n": "EH", "o": "FA", "p": "FB", "q": "FC", "r": "FD", "s": "FE", "t": "FF", "u": "FG", "v": "FH", "w": "GA", "x": "GB", "y": "GC", "z": "GD", "0": "GE", "1": "GF", "2": "GG", "3": "GH", "4": "HA", "5": "HB", "6": "HC", "7": "HD", "8": "HE", "9": "HF", "+": "HG", "/": "HH"}

keys=diccionarioN.keys()
diccionarioN2={}
for n in range(len(keys)):
	diccionarioN2[diccionarioN[keys[n]]]=keys[n]

keys=diccionarioL.keys()
diccionarioL2={}
for n in range(len(keys)):
	diccionarioL2[diccionarioL[keys[n]]]=keys[n]

if len(sys.argv)<2:
	imprimirAyuda()
elif sys.argv[1]=="-a":
	imprimirAyuda()
else:
	parametro=sys.argv[1]
	inIndex=0
	outIndex=0
	let=False
	for n in range(0,len(sys.argv)):
		if(sys.argv[n]=="-e"):
			inIndex=n+1
		if(sys.argv[n]=="-s"):
			outIndex=n+1
		if(sys.argv[n]=="-l"):
			let=True
	flag=False
	try:
		if(inIndex==0):
			raise ValueError
		file=sys.argv[inIndex]
		input=open(file, "rb")
		if(let and parametro=="-c"):
			diccionario=diccionarioL
		elif(let and parametro=="-d"):
			print("aqui")
			diccionario=diccionarioL2
		elif(parametro=="-d"):
			temp=open(file,"rb")
			temp=temp.read()
			if(str(temp[0]).isalpha()):
				diccionario=diccionarioL2
			else:
				diccionario=diccionarioN2
		elif(parametro=="-c"):
			diccionario=diccionarioN
		flag=True
	except ValueError:
		print("No hay archivo de entrada")
		imprimirAyuda()
	except:
		print("No se pudo abrir el archivo de entrada")	
	if (parametro=="-c" and flag):
		try:
			if outIndex==0:
				file2=file+".cif"
			else:
				file2=sys.argv[outIndex]
			if(not ("." in file2)):
				file2=file2+".cif"
			output=open(file2, "w")
			p=input.read(72)
			print("     Cifrando archivo....")
			while(p!=""):
				output.write(cifrar(base64.b64encode(p), diccionario))
				p=input.read(72)
			input.close()
			output.close()
			print("     Archivo cifrado!")
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
			output=open(file2, "w")
			p=input.read(72)
			print("     Decifrando archivo....")
			while(p!=""):
				output.write(base64.b64decode(descifrar(p, diccionario)))
				p=input.read(72)
			input.close()
			output.close()
			print("     Archivo decifrado!")
		except:
			print("No se pudo abrir el archivo de salida")
	elif(flag):		
		imprimirAyuda()
