# -*- coding: utf-8 -*-
"Criptoanalisis de Julio Cesar"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys
import hashlib

#Lee un archivo y retorna su hash en hexadecimal
def hashArchivo(archivo,metodo=hashlib.md5(),bloque=1000):
	buf = archivo.read(bloque)
	while(buf!=""):
		metodo.update(buf)
		buf = archivo.read(bloque)
	return metodo.hexdigest()

#Ordena de mayor a menor en un vector los caracteres mas repetidos dentro de cada subcriptograma(jotas)
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
			tabla=tabla+vector[n+i]+": "+str(d[vector[n+i]])+"\t"
		tabla=tabla+"\n"
	return tabla

def imprimirAyuda():
	print("analisisJulio.py es un programa para criptoanalizar un archivo cifrado usando el algoritmo de julio cesar. El programa retorna un log con las frecuencas y la clave, ademas del archivo decifrado")
	print("usando una clave")
	print(" ")
	print("SINTAXIS:")
	print("python analisisJulio.py archivo_a_criptoanalizar")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-a      Para ayuda                                                          |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python analisisJulio.py archivo.txt                                         |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")
	print("6-Noviembre-2014")

letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", '\x91', "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
alfabeto=28
#El tamaño de las cadenas que va a buscar
tamano=4
lineas=500

#Diccionarios para obtener el valor numerico de cada letra del alfabeto a utilizar y viceversa
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
	try:
		file=sys.argv[1]
		input=open(file, "rb")
	except:
		print("No se pudo abrir el archivo de entrada")	
	print("     Analizando.....")
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
		log.write(imprimirTabla(frec,vec))
		clave=obtenerClave(vec)
		if(clave==-1): 
			claves = []
			print("NO SE PUDO CRIPTOANALIZAR")
			break 
		else:
			log.write("CLAVE: "+posicionLetras[clave]+"\n \n")
			claves.append(clave)	
	input.seek(0)
	file2=file+".dec"
	output=open(file2,"w")
	p=input.read(1)
	while(p!=""):
		for k in claves:
			if(p==""): break
			mensaje=descifrar(p,k)
			if(ord(mensaje)==145): mensaje=chr(209)
			output.write(mensaje)
			p=input.read(1)
	log.close()
	logJotas.close()
	output.close()
	input.close()
	md5=open(file+".MD5","w")
	md5.write(file+": ")
	md5.write(hashArchivo(open(file,"rb"),hashlib.md5()))
	md5.write("\n"+file2+": ")
	md5.write(hashArchivo(open(file2,"rb"),hashlib.md5()))
	md5.close()	
	print("     Descifrado!")


