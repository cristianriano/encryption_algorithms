# -*- coding: utf-8 -*-
"Algoritmos de Criptografia"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys
import hashlib
import base64
import os

#Lee un archivo y retorna su hash en hexadecimal
def hashArchivo(archivo,metodo=hashlib.md5(),bloque=1000):
	buf = archivo.read(bloque)
	while(buf!=""):
		metodo.update(buf)
		buf = archivo.read(bloque)
	return metodo.hexdigest()

#---------------------------------------------TRANSPOSICION SIMPLE---------------------------------------
#Cifra con transposicion simple (2 bloques; caracteres impares y pares)
def cifrarSimple(frase):
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

def desSimple(crypto):
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

def imprimirAyudaSimple():
	print("Se cifra un archivo de texto usando el algoritmo de transposicion simple")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -t -cifrar_o_descifrar -e archivo_entrada -s archivo_salida")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python cripto.py -t -c -e entrada.txt -s salida.cif                         |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")

#---------------------------------------------TRANSPOSICION DOBLE---------------------------------------
#Cifra usando el algoritmo de transposicion doble (2 veces transposicion simple)
def cifrarDoble(frase):
	cryptoSimple=''
	cryptograma=''
	for n in range(0,len(frase),2):
		try:
			cryptoSimple=cryptoSimple+frase[n]
		except:
			pass	
		
	for n in range(1,len(frase),2):
		try:
			cryptoSimple=cryptoSimple+frase[n]
		except:
			pass
	for n in range(0,len(frase),2):
		try:
			cryptograma=cryptograma+cryptoSimple[n]
		except:
			pass
	for n in range(1,len(frase),2):
		try:
			cryptograma=cryptograma+cryptoSimple[n]
		except:
			pass
	return cryptograma

def desDoble(crypto):
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
	
	bloque1=mensaje[:lon]
	bloque2=mensaje[lon:]
	mensaje=''
	
	for n in range(0, lon):
		try:
			mensaje=mensaje+bloque1[n]
			mensaje=mensaje+bloque2[n]
		except:
			pass
	
	return mensaje

def imprimirAyudaDoble():
	print("Se cifra usando el algoritmo de transposcion doble para cifrar un archivo de texto")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -td -cifrar_descifrar -e archivo_entrada -s archivo_salida")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python cripto.py -td -c -e entrada.txt -s salida.cif                        |")
	print("-----------------------------------------------------------------------------")
	print("")
	print("AUTORES: ")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("4-Diciembre-2014")

#---------------------------------------------TRANSPOSICION POR GRUPOS --------------------------------

def cifrarGrupos(frase, llave):
	cryptograma=''
	for m in llave:
		cryptograma=cryptograma+frase[int(m)-1]		
	return cryptograma

def stuffGrupos(frase, llave):
	grupo=len(llave)
	relleno=grupo-(len(frase)%grupo)
	if(relleno==grupo):
		relleno=0
	for n in range(relleno):
		frase=frase+"#"
	return frase

def unstuffGrupos(cola,llave):
	cut=0
	for n in range(len(cola),0,-1):
		if(cola[n-1]!="#"):
			break
		else:
			cut=n
	cola=cola[:cut-1]
	return cola

def desGrupos(crypto, llave):
	mensaje=""
	grupo=len(llave)
	bloque1=[""]
	for n in range(1,grupo):
		bloque1.append("")
	for m in range(grupo):
		try:
			bloque1[int(llave[m])-1]=crypto[m]
		except:
			pass
	mensaje=mensaje+("".join(bloque1))
	return mensaje

def obtenerClaveGrupos(file3):
	clave1=open(file3, "rb")
	clave=[]
	claves=(clave1.read()).replace(" ","")
	claves=claves.replace("\n","")
	clave=claves.split(",")
	return clave

def verificarClaveGrupos(llave):
	tmp=sorted(llave)
	for n in range(len(llave)):
		if(not(tmp[n].isdigit())):
			print("La clave no es numerica")
			return False
		if(not(int(tmp[n])==n+1)):
			print("No es una clave valida")
			return False
	return True
	
def imprimirAyudaGrupos():
	print("Cifra un archivo de texto usando el algoritmo de transposicion por grupos usando una llave")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -tg -cifrar_descifrar -k clave -e archivo_entrada -s archivo_salida")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|-k      Especifica el archivo que contiene la clave                         |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python cripto.py -tg -c -k clave.txt -e entrada.txt -s salida.cif           |")
	print("|                                                                            |")
	print("|SINTAXIS CLAVE:                                                             |")
	print("|    5,3,1,2,4                                                               |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")

#----------------------------------------TRANSPOSICION POR SERIES-----------------------------------

def cifrarSeries(frase, serie):
	cryptograma=''
	for n in serie:
		cryptograma=cryptograma+frase[int(n)-1]
	return cryptograma
	
def stuffSeries(frase, serie):
	stuf=len(serie)-(len(frase)%len(serie))
	if(stuf==len(serie)):
		stuf=0
	for n in range(stuf):
		frase=frase+"#"
	return frase
	
def desSeries(crypto, serie):
	mensaje=''
	vector=[[]]*len(crypto)
	j=0
	for i in range(0,72,len(series)):
		for n in serie:
			try:
				vector[int(n)-1+i]=crypto[j]
			except:
				pass
			j=j+1
	cola=vector[len(vector)-len(serie):]
	for n in range(len(cola),0,-1):
		if(cola[n-1]=="#"):
			cola[n-1]=""
		else:
			break
	vector=vector[:len(vector)-len(serie)]
	mensaje="".join(vector)
	mensaje=mensaje+("".join(cola))
	return mensaje

def obtenerSerie(file2):
	input2=open(file2,"rb")
	funciones=[]
	for line in input2: 
			line=line.replace("\n","") 
			line=line.replace(" ","") 
			funcion=line.split(",") 
			funciones.append(funcion)
	serie=[]
	for n in range(len(funciones)):
		for m in range(len(funciones[n])):
			serie.append(funciones[n][m])
	return serie

def imprimirAyudaSeries():
	print("Cifra un archivo de texto usando el algoritmo de transposicion por series")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -ts -cifrar_descifrar -e archivo_entrada -k archivo_claves -s archivo_salida")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-k      Para archivo de clave                                               |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python cripto.py -ts -c -e entrada.txt -k clave.txt -s salida.cif           |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("")
	print("*El archivo clave de contener unicamente numeros")
	print("*Los elementos de cada funcion deben estar separados por coma (,)")
	print("*En el archivo deben estar todos los numeros desde 1 al mayor valor de la clave")
	print("EJEMPLO SINTAXIS PARA ARCHIVO ")
	print("1,3,5")
	print("2,8")
	print("6,4,7")
	print("-----------------------------------------------------------------------------")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")

#-----------------------------------------POLYBIOS--------------------------------------------

def cifrarPoly(frase, d):
	cryptograma=''
	for n in frase:
		try:
			cryptograma=cryptograma+d[n]
		except: 	
			cryptograma=cryptograma+n
	return cryptograma

def desPoly(crypto, d):
	mensaje=""
	for n in range(0,len(crypto),2):
		try:
			mensaje=mensaje+d[crypto[n:n+2]]
		except:
			mensaje=mensaje+crypto[n:n+2]
	return mensaje

	
def imprimirAyudaPoly():
	print("Cifra un archivo usando el algoritmo de sustitucion monoalfabetica de polybios, usando una matriz de numeros o letras")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -po -cifrado_decifrado -tipo_matriz -e archivo_entrada -s archivo_salida")
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
	print("|python cripto.py -po -c -n -e entrada.txt -s salida.cif                     |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")

#-------------------------------------------PLAYFAIR----------------------------------------------

def cifrarPlay(frase, d, m):
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

def desPlay(crypto, d, m):
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
	
def imprimirAyudaPlay():
	print("Cifra un archivo usando el algoritmo de sustitucion monoalfabetica, usando una matriz 8x8 con todos los caracteres de base 64, con una fila extra de caracteres especiales")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -pl -cifrado_decifrado -tipo_matriz -e archivo_entrada -s archivo_salida")
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
	print("|python playfair.py -pl -c -e entrada.txt -s salida.cif -k clave             |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("4-Diciembre-2014")

#----------------------------------------------AFIN---------------------------------------------------

def cifrarAfin(frase):
	cryptograma=''
	for n in frase:
		try:
			#Se calcula el indice del caracter cifrado
			m=((a*(base.index(n)))+b)%alfabeto
			cryptograma=cryptograma+base[m]
		except:
			#En caso de aparecer un igual no se cifra (pues no esta en los caracteres base 64)
			pass
	return cryptograma

def desAfin(crypto):
	mensaje=""
	for n in crypto:
		try:
			#Se calcula indice de decifrado (formula del algoritmo)
			m=((base.index(n)-b)*inverso)%alfabeto
			mensaje=mensaje+base[m]
		except:
			pass
	return mensaje


def calcularInverso(a,n):
#El inverso de a solo existe si son coprimos (MCD=1)
	if(MCD(n,a)==1):
		for m in range(1,n-1):
#Se prueba la condicion de inverso
			if((a*m)%n==1):
				return m
	else:
		raise ValueError
#Funcion que calcula el Maximo Comun Divisor	
def MCD(x,y):
	tmp = x%y
	if(tmp==0):
		return y
	elif(tmp==1):
		return 1
	else:
		return MCD(y,tmp)

def imprimirAyudaAfin():
	print("Cifra un archivo usando el algoritmo de cifrado afin, usando 2 parametros A y B. Ambos deben ser menores que 64 y ademas A y 64 deben ser coprimos")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -af -cifrado_decifrado -e archivo_entrada -s archivo_salida -A numeroA -B numeroB")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c      Para cifrar                                                         |")
	print("|-d      Para descifrar                                                      |")
	print("|-a      Para ayuda                                                          |")
	print("|-e      Definir archivo de entrada                                          |")
	print("|-s      Definir archivo de salida (opcional)                                |")
	print("|-A      Parametro A                                                         |")
	print("|-B      Parametro B                                                         |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python cripto.py -af -c -e entrada.txt -s salida.cif -A 15 -B 3             |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")

#-------------------------------------------VIGENERE-------------------------------------------------

def cifrarVig(frase, clave):
	cryptograma=''
	for n in range(longitud):
		try:
			#Se calcula el indice del caracter cifrado
				i=((base.index(frase[n]))+(base.index(clave[n])))%alfabeto
				cryptograma=cryptograma+base[i]	
		except:
			pass
	return cryptograma

def desVig(crypto, clave):
	mensaje=""
	for n in range(longitud):
		try:
			#Se calcula indice de decifrado (formula del algoritmo)
			i=((base.index(crypto[n]))-(base.index(clave[n])))%alfabeto
			mensaje=mensaje+base[i]
		except:
			pass
	return mensaje

def imprimirAyudaVig():
	print("Cifra un archivo usando el algoritmo de vigenere usando una clave")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -vi -cifrado_decifrado -e archivo_entrada -s archivo_salida -k archivo_clave")
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
	print("|python cripto.py -vi -c -e entrada.txt -s salida.cif -k clave.txt           |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")


def armarClaveVig(fileClave):
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
	return clave

#-----------------------------------------JULIO CESAR-------------------------------------------

def cifrarJulio(cripto, k):
	mensaje=""
	for n in cripto:
		try:
			mensaje=mensaje+posicionLetras[(letrasPosicion[n]+k)%alfabeto]	
		except:
			mensaje=mensaje+n
	return mensaje

def desJulio(cripto, k):
	mensaje=""
	for n in cripto:
		try:
			if(ord(n)==195): continue
			elif(ord(n)==145): 
				mensaje=mensaje+posicionLetras[(14-k)%alfabeto]
			else:
				mensaje=mensaje+posicionLetras[(letrasPosicion[n]-k)%alfabeto]	
		except:
			mensaje=mensaje+n
	return mensaje

	
def imprimirAyudaJulio():
	print("Cifrar un archivo de texto usando el algoritmo de sustitucion monoalfabetica de Julio Cesar")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -ju -cifrado_decifrado -k clave -e archivo_entrada -s archivo_salida")
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
	print("|python cripto.py -ju -c -e entrada.txt -s salida.cif -k R                   |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")


#--------------------------------------------ANALISIS DE FRECUENCIAS---------------------------

def armarVector(d):
	v=d.keys()
	vector=[]
	cantidad=0
	maximo=-1
	num=0
	while(v!=[]):
		for n in range(len(v)):
			cantidad=d[v[n]]	
			if(cantidad>=maximo):
				maximo=cantidad
				num=n
		vector.append(v[num])
		v.remove(v[num])
		maximo=-1
		num=0
	return vector


def desFrec(cripto, k):
	mensaje=""
	for n in cripto:
		try:
			if(ord(n)==195): continue
			elif(ord(n)==145):
				mensaje=mensaje+posicionLetras[(14-k)%alfabeto]
			else:	 
				mensaje=mensaje+posicionLetras[(letrasPosicion[n]-k)%alfabeto]	
		except:
			mensaje=mensaje+n
	return mensaje

def imprimirTablaFrec(d):
	tabla="TABLA DE FRECUENCIAS: \n"
	for n in range(0,len(vector),4):
		for i in range(4):
			tabla=tabla+vector[n+i]+": "+str(d[vector[n+i]])+"\t"
		tabla=tabla+"\n"
	return tabla


def obtenerClaveFrec(vector):
	flag=False
	clave=-1		
	for i in range(0, 4):
		for j in range(0, 4):
			if(letrasPosicion[vector[i]]-letrasPosicion[vector[j]]==4):
				clave=letrasPosicion[vector[j]]
				flag=True
				break
		if(flag):
			break
	return clave
letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 'Ñ', "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
alfabeto=28
letrasPosicion={}
for n in range(alfabeto):
	letrasPosicion[letras[n]]=n

k=letrasPosicion.keys()
posicionLetras={}

for n in k:
	posicionLetras[letrasPosicion[n]]=n

def imprimirAyudaFrec():
	print("Criptoanaliza un archivo cifrado usando el algoritmo de julio cesar. El programa retorna un log con las frecuencas y la clave, ademas del archivo decifrado")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -aj archivo_a_criptoanalizar")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-a      Para ayuda                                                          |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python cripto.py -aj -e archivo.txt                                         |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")

#-------------------------------------------KASISKI----------------------------------------------------

#Funcion para descifrar algoritmo de sustitucion monoalfabetica (Julio Cesar)
def descifrar(cripto, k):
	if(cripto==""): return ""
	if(ord(cripto)==195): cripto=input.read(1)
	if(ord(cripto)==145 or ord(cripto)==209): return posicionLetras[(14-k)%alfabeto]
	return posicionLetras[(letrasPosicion[cripto]-k)%alfabeto]


#Funcion que obtiene un caracter de la clave a partir de uno de los subcriptogramas generado por obtenerJotas
def obtenerClave(vector):
	clave=-1
	for i in range(5):
		for j in range(i):
			if(((letrasPosicion[vector[j]]-4)%(alfabeto+1)) == letrasPosicion[vector[0]]):
				clave = letrasPosicion[vector[0]]
				return clave
			if(((letrasPosicion[vector[j]]-4)%(alfabeto)) == letrasPosicion[vector[1]]):
				clave = letrasPosicion[vector[1]]
				return clave
			if(((letrasPosicion[vector[j]]-4)%(alfabeto)) == letrasPosicion[vector[2]]):
				clave = letrasPosicion[vector[2]]
				return clave
			if(((letrasPosicion[vector[j]]-4)%(alfabeto)) == letrasPosicion[vector[3]]):
				clave = letrasPosicion[vector[3]]
				return clave
	return clave

#Funcion que obtiene un numero de subcriptogramas igual a la longitud de la clave
def obtenerJotas(cripto, num):
	Jotas = []
	cripto=cripto.replace('\xc3',"")
	for index in range(0, num):
		msj = ""
		for i in range(index, len(cripto), num):
			msj = msj + cripto[i]
		Jotas.append(msj)
	return Jotas

#Analisis para obtener las letras que mas repetien en los criptogramas obtenidos de la funcion obtenerJotas
def obtenerFrec(jota):
	frecuencias = {}
	for i in range(alfabeto):
		letra=letras[i]
		cantidad=0
		cantidad=cantidad+jota.count(letra)
		frecuencias[letra]=cantidad
	return frecuencias

def imprimirTabla(d,vector):
	tabla="TABLA DE FRECUENCIAS: \n"
	for n in range(0,len(vector),4):
		for i in range(4):
			tabla=tabla+vector[n+i]+": "+str(d[vector[n+i]])+" -\t-"
		tabla=tabla+"\n"
	return tabla

def imprimirAyudaKa():
	print("Criptoanaliza un archivo de texto cifrado usando el algoritmo de Vigenere. El programa retorna un log con las frecuencias y la clave, ademas del archivo decifrado. Tambien retorna un archivo con subcriptogramas analizados")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -ka -e archivo_a_criptoanalizar")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-a      Para ayuda                                                          |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python cripto.py -ka -e archivo.txt                                         |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")

#Funcion que calcula el Maximo Comun Divisor	
def MCD(vec):
	m=vec[0]
	for n in vec:
		m=min(m,n)
	return MCDvector(vec,m)

def MCDvector(v,m):
	for i in range(m,0,-1):
		flag=True
		for n in v:
			if(n%i==0): continue
			else:
				flag=False
				break
		if(flag): return i


#-------------------------------------------INICIO CODIGO----------------------------------------------
def imprimirAyuda():
	print("cripto.py es un programa que brinda la posibilidad de cifrar un archivo con 9 diferentes algoritmos. Adicional a esto brinda las herramientas para criptoanalizar un archivo por medio del analisis de frecuencias o aplicando el metodo de kasiski")
	print(" ")
	print("Dependiendo del algoritmo se le pediran al usuario distintos tipos de parametros, como claves numericas o passwords.")
	print("Para obtener mas ayuda acerca de un algoritmo en particular escriba la bandera del algoritmo sin ningun otro parametro")
	print(" ")
	print("SINTAXIS:")
	print("python cripto.py -algoritmo -cifado_decifrado -e archivo_entrada -parametro1 ... -parametro n")
	print("-----------------------------------------------------------------------------")
	print("|ALGORITMOS:                                                                 |")
	print("|-t      Transposicion simple                                                |")
	print("|-td     Transposicion doble                                                 |")
	print("|-tg     Transposicion por grupos                                            |")
	print("|-ts     Transposicion por series                                            |")
	print("|-po     Polybios                                                            |")
	print("|-pl     Playfair                                                            |")
	print("|-af     Cifrado Afin                                                        |")
	print("|-ju     Julio Cesar                                                         |")
	print("|-vi     Vigenere                                                            |")
	print("|                                                                            |")
	print("|CRIPTOANALISIS:                                                             |")
	print("|-aj     Analsis de frecuencias (Criptoanalisis julio cesar)                 |")
	print("|-ka     Metodo de Kasiski                                                   |")
	print("|                                                                            |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("4-Diciembre-2014")

base=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/", "!", '"', "#", "$", "%", "&", "(", ")"]

alfabeto=64

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
	algoritmo=sys.argv[1]
	if(len(sys.argv)==2):
		if(algoritmo=="-t"): 
			imprimirAyudaSimple()
			sys.exit(0)
		elif(algoritmo=="-td"): 
			imprimirAyudaDoble()
			sys.exit(0)
		elif(algoritmo=="-ts"): 
			imprimirAyudaSeries()
			sys.exit(0)
		elif(algoritmo=="-tg"): 
			imprimirAyudaGrupos()
			sys.exit(0)
		elif(algoritmo=="-po"): 
			imprimirAyudaPoly()		
			sys.exit(0)
		elif(algoritmo=="-pl"): 
			imprimirAyudaPlay()
			sys.exit(0)
		elif(algoritmo=="-af"): 
			imprimirAyudaAfin()
			sys.exit(0)
		elif(algoritmo=="-vi"): 
			imprimirAyudaVi()
			sys.exit(0)
		elif(algoritmo=="-ka"): 
			imprimirAyudaKa()	
			sys.exit(0)
		elif(algoritmo=="-aj"): 
			imprimirAyudaFrec()
			sys.exit(0)
		elif(algoritmo=="-ju"): 
			imprimirAyudaJulio()
			sys.exit(0)
		else:
			imprimirAyuda()
			sys.exit(0)
	parametro=sys.argv[2]
	inIndex=0
	outIndex=0
	kIndex=0
	let=False
	aIndex=0
	bIndex=0
	ay=False
	for n in range(0,len(sys.argv)):
		if(sys.argv[n]=="-e"):
			inIndex=n+1
		if(sys.argv[n]=="-s"):
			outIndex=n+1
		if(sys.argv[n]=="-k"):
			kIndex=n+1
		if(sys.argv[n]=="-l"):
			let=True
		if(sys.argv[n]=="-A"):
			aIndex=n+1
		if(sys.argv[n]=="-B"):
			bIndex=n+1
		if(sys.argv[n]=="-a"):
			ay=True
	if(not ay):	
		try:
			if(inIndex==0):
				raise ValueError
			file=sys.argv[inIndex]
			file2=file+".new"
		except ValueError:
			print("No hay archivo de entrada")
			sys.exit(0)
		except:
			print("No se pudo abrir el archivo de entrada")	
			sys.exit(0)

	if(algoritmo=="-t"):	#TRANSPOSICION SIMPLE
		if(parametro=="-c"):
			try:
				if outIndex==0:
					file2=file+".cif"
				else:
					file2=sys.argv[outIndex]	
				print("   Cifrando....")
				input=open(file,"rb")
				output=open(file2,"w")
				p=input.read(72)
				while(p!=""):
					output.write(cifrarSimple(p))
					p=input.read(72)
				print("   Cifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		elif(parametro=="-d"):
			try:
				if outIndex==0:
					file2=file+".dec"
				else:
					file2=sys.argv[outIndex]	
				input=open(file,"rb")
				output=open(file2,"w")
				print("   Descifrando....")
				p=input.read(72)
				while(p!=""):
					output.write(desSimple(p))
					p=input.read(72)
				print("   Descifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		else:
			imprimirAyudaSimple()
			sys.exit(0)

	elif(algoritmo=="-td"):	#TRANSPOSICION DOBLE
		if(parametro=="-c"):
			try:
				if outIndex==0:
					file2=file+".cif"
				else:
					file2=sys.argv[outIndex]	
				print("   Cifrando....")
				input=open(file,"rb")
				output=open(file2,"w")
				p=input.read(72)
				while(p!=""):
					output.write(cifrarDoble(p))
					p=input.read(72)
				print("   Cifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		elif(parametro=="-d"):
			try:
				if outIndex==0:
					file2=file+".dec"
				else:
					file2=sys.argv[outIndex]	
				input=open(file,"rb")
				output=open(file2,"w")
				print("   Descifrando....")
				p=input.read(72)
				while(p!=""):
					output.write(desDoble(p))
					p=input.read(72)
				print("   Descifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		else:
			imprimirAyudaDoble()
			sys.exit(0)

	elif(algoritmo=="-tg"):	#TRANSPOSICION GRUPOS
		if(parametro=="-c"):
			try:
				if outIndex==0:
					file2=file+".cif"
				else:
					file2=sys.argv[outIndex]	
				if(kIndex==0): 
					raise NameError
				clave=obtenerClaveGrupos(sys.argv[kIndex])
				if(not verificarClaveGrupos(clave)): 
					raise TypeError
				print("   Cifrando....")
				input=open(file,"rb")
				output=open(file2,"w")
				t=len(clave)
				p=input.read(t)
				while(len(p)==t):
					output.write(cifrarGrupos(p, clave))
					p=input.read(t)
				if(len(p)>0):
					output.write(cifrarGrupos(stuffGrupos(p,clave), clave))
				print("   Cifrado!")
				input.close()
				output.close()
			except NameError:
				print("No hay archivo de clave")
				sys.exit(0)
			except TypeError:
				print("Error en la clave")	
				sys.exit(0)
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		elif(parametro=="-d"):
			try:
				if outIndex==0:
					file2=file+".dec"
				else:
					file2=sys.argv[outIndex]	
				if(kIndex==0): 
					raise NameError
				clave=obtenerClaveGrupos(sys.argv[kIndex])
				if(not verificarClaveGrupos(clave)): 
					raise TypeError
				print("   Descifrando....")	
				input=open(file,"rb")
				output=open(file2,"w")
				t=len(clave)
				p=input.read(t)
				while(True):
					q=input.read(t)
					if(q!=""):
						output.write(desGrupos(p, clave))
						p=q
					else:
						break
				if(len(p)>0):
					q=desGrupos(p,clave)
					output.write(unstuffGrupos(q,clave))
				print("   Descifrado!")
				input.close()
				output.close()
			except NameError:
 				print("No hay archivo de clave")
				sys.exit(0)
			except TypeError:
				print("Error en la clave")
				sys.exit(0)
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		else:
			imprimirAyudaGrupos()
			sys.exit(0)
	elif(algoritmo=="-ts"):	#TRANSPOSICION SERIES
		if(parametro=="-c"):
			try:
				if outIndex==0:
					file2=file+".cif"
				else:
					file2=sys.argv[outIndex]	
				if(kIndex==0): 
					raise NameError
				series=obtenerSerie(sys.argv[kIndex])
				print("   Cifrando....")
				input=open(file,"rb")
				output=open(file2,"w")
				p=input.read(len(series))
				while(len(p)==len(series)):
					output.write(cifrarSeries(p,series))
					p=input.read(len(series))
				if(len(p)>0):
					output.write(cifrarSeries(stuffSeries(p,series),series))
				print("   Cifrado!")
				input.close()
				output.close()
			except NameError:
				print("No hay archivo de clave")
				sys.exit(0)
			except TypeError:
				print("Error en la clave")
				sys.exit(0)
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		elif(parametro=="-d"):
			try:
				if outIndex==0:
					file2=file+".dec"
				else:
					file2=sys.argv[outIndex]	
				if(kIndex==0): 
					raise NameError
				series=obtenerSerie(sys.argv[kIndex])
				print("   Descifrando....")	
				input=open(file,"rb")
				output=open(file2,"w")
				size=len(input.read())
				input.seek(0)
				for n in range(0,size,72):
					output.write(desSeries(input.read(72),series))
				print("   Descifrado!")
				input.close()
				output.close()
			except NameError:
				print("No hay archivo de clave")
				sys.exit(0)
			except TypeError:
				print("Error en la clave")
				sys.exit(0)
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		else:
			imprimirAyudaSeries()
			sys.exit(0)
	elif(algoritmo=="-po"):	#POLYBIOS
		if(parametro=="-c"):
			try:
				if outIndex==0:
					file2=file+".cif"
				else:
					file2=sys.argv[outIndex]
				if(let):
					diccionario=diccionarioL
				else:
					diccionario=diccionarioN	
				print("   Cifrando....")
				input=open(file,"rb")
				output=open(file2,"w")
				p=input.read(72)
				while(p!=""):
					output.write(cifrarPoly(base64.b64encode(p), diccionario))
					p=input.read(72)
				print("   Cifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		elif(parametro=="-d"):
			try:
				if outIndex==0:
					file2=file+".dec"
				else:
					file2=sys.argv[outIndex]
				if(let):
					diccionario=diccionarioL2
				else:
					diccionario=diccionarioN2		
				input=open(file,"rb")
				output=open(file2,"w")
				print("   Descifrando....")
				p=input.read(72)
				while(p!=""):
					output.write(base64.b64decode(desPoly(p, diccionario)))
					p=input.read(72)
				print("   Descifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		else:
			imprimirAyudaPoly()
			sys.exit(0)
	elif(algoritmo=="-pl"):	#PLAYFAIR
		try:
			if(kIndex==0): raise TypeError
			file2=sys.argv[kIndex]
			input2=open(file2,"r")
			for line in input2:
				list="-".join(str(line)).split("-",len(line))
			#Remueve el enter que agregan los editores de texto al final (enter)
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
		except TypeError:
			print("No ingreso un archivo con la clave")
		if(parametro=="-c"):
#			try:
				if outIndex==0:
					file2=file+".cif"
				else:
					file2=sys.argv[outIndex]
				print("   Cifrando....")
				input=open(file,"rb")
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
					output.write(cifrarPlay(p, diccionario, matriz))
					p=tmp.read(350)
				tmp.close()
				output.close()
				os.remove(file+".tmp")
				print("   Cifrado!")
				input.close()
				output.close()
#			except:
#				print("No se pudo abrir el archivo de salida")
#				sys.exit(0)
		elif(parametro=="-d"):
#			try:
				if outIndex==0:
					file2=file+".dec"
				else:
					file2=sys.argv[outIndex]		
				input=open(file,"rb")
				output=open(file2,"w")
				print("   Descifrando....")
				temp = ""
				p=input.read(350)
				while(p!=""):
					temp = temp + desPlay(p, diccionario, matriz)
					p=input.read(350)
				output.write(base64.b64decode(temp))
				input.close()
				output.close()
				print("   Descifrado!")
#			except:
#				print("No se pudo abrir el archivo de salida")
#				sys.exit(0)
		else:
			imprimirAyudaPlay()
			sys.exit(0)
	elif(algoritmo=="-af"):	#AFIN
		try:
			if(aIndex==0 or bIndex==0):
				raise NameError
			a=int(sys.argv[aIndex])
			b=int(sys.argv[bIndex])
			#Verificar condiciones de a y b para el algoritmo
			if(a>=alfabeto or b>=alfabeto):
				raise ZeroDivisionError
			if(MCD(alfabeto,a)!=1):
				raise ZeroDivisionError
		except NameError:
			print("No ingreso los parametros A y B")
			sys.exit(0)
		except ZeroDivisionError:
			print("A Y B no cumplen con las condiciones")
			sys.exit(0)
		except:
			pass
		if(parametro=="-c"):
			try:
				if outIndex==0:
					file2=file+".cif"
				else:
					file2=sys.argv[outIndex]
				print("   Cifrando....")
				input=open(file,"rb")
				output=open(file2,"w")
				p=input.read(72)
				while(p!=""):
					output.write(cifrarAfin(base64.b64encode(p)))
					p=input.read(72)
				print("   Cifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		elif(parametro=="-d"):
			try:
				if outIndex==0:
					file2=file+".dec"
				else:
					file2=sys.argv[outIndex]
				input=open(file,"rb")
				output=open(file2,"w")
				tmp=open(file+".tmp","w")
				print("   Decifrando....")
				inverso=calcularInverso(a,alfabeto)
				p=input.read(600)
				while(p!=""):
					tmp.write(desAfin(p))
					p=input.read(600)
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
				while(p!=""):
					output.write(base64.b64decode(p))
					p=tmp.read(600)
				tmp.close()
				output.close()
				os.remove(file+".tmp")
				print("   Descifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		else:
			imprimirAyudaAfin()
			sys.exit(0)
	elif(algoritmo=="-vi"):	#VIGENERE
		if(parametro=="-a"):
			imprimirAyudaVig()
			sys.exit(0)
		try:
			if(kIndex==0):
				raise TypeError
			clave=armarClaveVig(sys.argv[kIndex])
			longitud=len(clave)
		except TypeError:
			print("No hay archivo de claves")
			sys.exit(0)
		except:
			pass
		if(parametro=="-c"):
			try:
				if outIndex==0:
					file2=file+".cif"
				else:
					file2=sys.argv[outIndex]	
				print("   Cifrando....")
				tmp=open(file+".tmp","w")
				input=open(file,"rb")
				output=open(file2,"w")
				p=input.read(600)
				while(p!=""):
					tmp.write(base64.b64encode(p))
					p=input.read(600)
				tmp.close()
				input.close()
				tmp=open(file+".tmp","rb")
				p=tmp.read(longitud)
				while(p!=""):
					output.write(cifrarVig(p, clave))
					p=tmp.read(longitud)
				tmp.close()
				output.close()
				os.remove(file+".tmp")
				print("   Cifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		elif(parametro=="-d"):
			try:
				if outIndex==0:
					file2=file+".dec"
				else:
					file2=sys.argv[outIndex]	
				input=open(file,"rb")
				output=open(file2,"w")
				tmp=open(file+".tmp","w")
				print("   Descifrando....")
				p=input.read(longitud)
				while(p!=""):
					tmp.write(desVig(p, clave))
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
				print("   Descifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		else:
			imprimirAyudaVig()
			sys.exit(0)
	elif(algoritmo=="-ju"):	#JULIO
		print("!")
		if(parametro=="-a"):
			imprimirAyudaJulio()
			sys.exit(0)
		try:
			print("!")
			if(kIndex==0):
				raise TypeError
			clave=letrasPosicion[(sys.argv[kIndex])]
			alfabeto=28
		except TypeError:
			print("No ingreso una clave")
			sys.exit(0)
		except:
			pass
		if(parametro=="-c"):
			try:
				if outIndex==0:
					file2=file+".cif"
				else:
					file2=sys.argv[outIndex]	
				print("   Cifrando....")
				input=open(file,"rb")
				output=open(file2,"w")
				p=input.read(72)
				while(p!=""):
					output.write(cifrarJulio(p, clave))
					p=input.read(72)
				print("   Cifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		elif(parametro=="-d"):
			try:
				if outIndex==0:
					file2=file+".dec"
				else:
					file2=sys.argv[outIndex]	
				input=open(file,"rb")
				output=open(file2,"w")
				print("   Descifrando....")
				p=input.read(72)
				while(p!=""):
					output.write(desJulio(p, clave))
					p=input.read(72)
				print("   Descifrado!")
				input.close()
				output.close()
			except:
				print("No se pudo abrir el archivo de salida")
				sys.exit(0)
		else:
			imprimirAyudaJulio()
			sys.exit(0)
	elif(algoritmo=="-aj"):	#ANALISIS JULIO
		if(parametro=="-a"):
			imprimirAyudaFrec()
			sys.exit(0)
		else:
			alfabeto=28
			lineas=300
			frecuencias={}
			try:
				input=open(file, "rb")
			except:
				print("No se pudo abrir el archivo de entrada")	
				sys.exit(0)
			print("   Analizando.....")
			for i in range(alfabeto):
				p=input.read(lineas)
				letra=letras[i]
				cantidad=0
				while(p!=""):
					cantidad=cantidad+p.count(letra)
					p=input.read(lineas)
				frecuencias[letra]=cantidad
				input.seek(0)

			vector=armarVector(frecuencias)
			clave=obtenerClaveFrec(vector)
			if(clave==-1):
				print("   No se puedo decifrar")
				sys.exit(0)
			else:	
				log=open(file+".log","w")
				log.write(imprimirTabla(frecuencias)+"\n")
				log.write("CLAVE: "+str(posicionLetras[clave]))
				log.close()

				file2=file+".dec"
				output=open(file2,"w")
				p=input.read(lineas)
				while(p!=""):
					output.write(desFrec(p,clave))
					p=input.read(lineas)
				input.close()
				output.close()
				print("   Descifrado!")
	elif(algoritmo=="-ka"):	#KASISKI
		if(parametro=="-a"):
			imprimirAyudaKa()
			sys.exit(0)
		else:
			letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", '\x91', "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
			alfabeto=28
			letrasPosicion={}
			for n in range(alfabeto):
				letrasPosicion[letras[n]]=n

			k=letrasPosicion.keys()
			posicionLetras={}

			for n in k:
				posicionLetras[letrasPosicion[n]]=n

			tamano=4
			try:
				input=open(file, "rb")
			except: 
				print("No se pudo abrir el archivo de entrada")	
				sys.exit(0)
			print("   Analizando.....")
			#Se crea el diccionario donde se van a guardar las cadenas y la posicion en el texto donde aparece. Se guardan todas asi aparezcan una sola vez (hace mas eficiente el codigo y mas rapido)
			cadenas={}
			p1=input.read()
			p1=p1.replace("\xc3","")
			#Cuando i llegue a 0 quiere decir que se han leido los caracteres suficientes para crear una cadena del tamaño requerido (4 en este caso)
			pos=0
			p=p1[pos]
			pos+=1
			i=-tamano
			while(True):
				if(pos>=len(p1)): break
				c=p1[pos]
				pos+=1
				#Se verifica que no se haya acabado de leer el codigo
				#Se concatena el caracter leido en p
				p=p+c
				i+=1
				if(i>=0):
				#Se almacena la posicion y la cadena, si esta repetida se separa por un espacio la nueva posicion
					try:
						cadenas[p[i:i+tamano]]=cadenas[p[i:i+tamano]]+" "+str(pos)
					except:
						cadenas[p[i:i+tamano]]=str(pos)	

			#Se almacena en un diccionario diferente las cadenas que aparecen mas de una vez
			repetidas={}
			for n in cadenas.keys():
				if(" " in cadenas[n]):
					#Se almacenan las distacias en un vector. Por algun motivo no se dejaba desde la linea 162 donde se almacena
					repetidas[n]=cadenas[n].split(" ")

			llaves=repetidas.keys()
			numCadenasUsadas=[]
			valores=[]
			posiblesL={}
			longitud=0
			ls=0
			for i in range(0,len(llaves),4):
				for n in range(4):
					t=repetidas[llaves[i+n]]
					for j in t:
						d=int(j)-int(t[0])
						if(d!=0 and not(d in valores)): 
							valores.append(d)
				longitud=MCD(valores)
				if(longitud!=1): 
					ls+=1
					try:
						posiblesL[longitud]=posiblesL[longitud]+1
					except:
						numCadenasUsadas.append((i,longitud))
						posiblesL[longitud]=1
				if(ls>=15): break
				valores=[]
			ll=posiblesL.keys()
			maximo=1
			longitud=0
			for n in ll:
				if(posiblesL[n]>=maximo):
					maximo=posiblesL[n]
					longitud=n
			for n in numCadenasUsadas:
				if(n[1]==longitud): i=n[0]
			cadenasUsadas=[llaves[i],llaves[i+1],llaves[i+2],llaves[i+3]]
			input.seek(0)
			#ALVIS
			cr = input.read()
			js = obtenerJotas(cr,longitud)  
			claves = []
			logJotas = open(file+".jotas","w")
			log=open(file+".log","w")
			log.write("CADENAS \n \n" )
			log.write(cadenasUsadas[0]+":  "+cadenas[cadenasUsadas[0]]+"\n")
			log.write(cadenasUsadas[1]+":  "+cadenas[cadenasUsadas[1]]+"\n")
			log.write(cadenasUsadas[2]+":  "+cadenas[cadenasUsadas[2]]+"\n")
			log.write(cadenasUsadas[3]+":  "+cadenas[cadenasUsadas[3]]+"\n \n")
			log.write("LONGITUD: "+str(longitud)+"\n \n")
			for n in range(len(js)):
				logJotas.write("JOTA #"+str(n)+":\n")
				logJotas.write(js[n]+"\n \n \n")
				frec = obtenerFrec(js[n])
				vec = armarVector(frec)
				clave=obtenerClave(vec)
				log.write(imprimirTabla(frec,vec))
				if(clave==-1): 
					claves = []
					print("NO SE PUDO CRIPTOANALIZAR")
					break 
				else:
					log.write("CLAVE: "+posicionLetras[clave]+"\n \n")
					claves.append(clave)	
			log.write("CLAVE: ")
			w=""
			for n in claves:
				log.write(str(posicionLetras[n]))
				w=w+str(posicionLetras[n])
			input.seek(0)
			file2=file+".dec"
			output=open(file2,"w")
			p=input.read(1)
			while(p!=""):
				for k in claves:
					if(p==""): break
					mensaje=descifrar(p,k)
					if(ord(mensaje[0])==145): mensaje=chr(209)
					output.write(mensaje)
					p=input.read(1)
			log.close()
			logJotas.close()
			output.close()
			input.close()
			print("   Descifrado!")



	md5=open(file+".MD5","w")
	md5.write(file+": ")
	md5.write(hashArchivo(open(file,"rb"),hashlib.md5()))
	md5.write("\n"+file2+": ")
	md5.write(hashArchivo(open(file2,"rb"),hashlib.md5()))
	md5.close()

