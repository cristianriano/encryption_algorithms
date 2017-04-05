"Algoritmo Cryptografico de Playfair"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
# -*- coding: 850 -*-
import sys
import base64
import os

def cifrar(frase, d, m):
	cryptograma=''
	try:
		fr = frase[:frase.index("=")]
	except: 	
		fr = frase
	NumIguales= len(frase)-len(fr)
	for i in range(0,len(fr),2):
		try:
			if(fr[i]==fr[i+1]):
				fr = fr[:i+1]+"#"+fr[i+1:]
		except:
			pass
	while(len(fr)%2!=0):
		try:
			stuf=tmp.read(1)
			if (stuf==""):
	 			raise TypeError
			fr=fr+stuf
		except:
			fr = fr + "#"
		
	while fr!="":
		try:
			if(d[fr[0]][0]==d[fr[1]][0]):
				cryptograma=cryptograma+m[d[fr[0]][0]][(d[fr[0]][1]+1)%8]+m[d[fr[1]][0]][(d[fr[1]][1]+1)%8]
				fr=fr[2:]
			elif(d[fr[0]][1]==d[fr[1]][1]):
				cryptograma=cryptograma+m[(d[fr[0]][0]+1)%9][d[fr[0]][1]]+m[(d[fr[1]][0]+1)%9][d[fr[1]][1]]
				fr=fr[2:]
			else:
				cryptograma=cryptograma+m[d[fr[0]][0]][d[fr[1]][1]]+m[d[fr[1]][0]][d[fr[0]][1]]
				fr=fr[2:]
		except:
			pass			
	cryptograma= cryptograma + ("="*NumIguales)
	return cryptograma

def descifrar(crypto, d, m):
	mensaje=""
	try:
		cr = crypto[:crypto.index("=")]
	except: 	
		cr = crypto
	NumIguales= len(crypto)-len(cr)
	while cr!="":
		try:
			if(d[cr[0]][0]==d[cr[1]][0]):  #misma fila
				mensaje=mensaje+m[d[cr[0]][0]][(d[cr[0]][1]-1)%8]+m[d[cr[1]][0]][(d[cr[1]][1]-1)%8]
				cr=cr[2:]
			elif(d[cr[0]][1]==d[cr[1]][1]): #misma columna
				mensaje=mensaje+m[(d[cr[0]][0]-1)%9][d[cr[0]][1]]+m[(d[cr[1]][0]-1)%9][d[cr[1]][1]]
				cr=cr[2:]
			else: 				#distinta fila y distinta columna
				mensaje=mensaje+m[d[cr[0]][0]][d[cr[1]][1]]+m[d[cr[1]][0]][d[cr[0]][1]]
				cr=cr[2:]
		except:
			pass
	
	mensaje = mensaje.replace("#","")
	mensaje = mensaje + ("="*NumIguales)
	return mensaje
	
def imprimirAyuda():
	print("playfair.py es un programa para cifrar un archivo usando el algoritmo de")
	print("sustitucion monoalfabetica, usando una matriz 8x8 con todos los caracteres")
	print("de base 64, con una fila extra de caracteres especiales")
	print(" ")
	print("SINTAXIS:")
	print("python playfair.py -cifrado_decifrado -tipo_matriz -e archivo_entrada -s archivo_salida")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|-k      Para definir el archivo con la clave                                |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python playfair.py -c -e entrada.txt -s salida.cif -k clave                 |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")

base=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/", "!", '"', "#", "$", "%", "&", "(", ")"]

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
		if(sys.argv[n]=="-k"):  
			funIndex=n+1
	flag=False
	try:
		if(inIndex==0):
			raise ValueError
		if(funIndex==0):
			raise NameError

		file=sys.argv[inIndex]
		input=open(file, "rb")
		file2=sys.argv[funIndex]
		input2=open(file2,"r")
		for line in input2:
			list="-".join(str(line)).split("-",len(line))
		#Remueve el enter que agregan los editores de texto al final
		list.pop()
		clave=[]
		for key in list:
			if key not in clave:
				clave.append(key)
		for key in base:
			if key not in clave:
				clave.append(key)
		matriz=[]
		while clave != []:
			matriz.append(clave[:8])
			clave=clave[8:]
		diccionario={}
		for n in range(9):
			for m in range(8):	
				diccionario[matriz[n][m]]=[n,m]			
		flag=True
	
	except ValueError:
		print("No hay archivo de entrada")
		imprimirAyuda()
	except NameError:
		print("No hay archivo de clave")
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
			p=input.read(600)
			while(p!=""):
				tmp.write(base64.b64encode(p))
				p=input.read(600)
			tmp.close()
			input.close()
			tmp=open(file+".tmp","rb")
			p=tmp.read(350)
			output=open(file2, "w")
			while(p!=""):
				output.write(cifrar(p, diccionario, matriz))
				p=tmp.read(350)
			tmp.close()
			output.close()
			os.remove(file+".tmp")
		except:
			print("No se pudo abrir el archivo de salida")
		
	
	elif(parametro=="-d" and flag):
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
			temp = ""
			p=input.read(350)
			while(p!=""):
				temp = temp + descifrar(p, diccionario, matriz)
				p=input.read(350)
			output.write(base64.b64decode(temp))
			input.close()
			output.close()
		except:
			print("No se pudo abrir el archivo de salida")
	elif(flag):		
		imprimirAyuda()
