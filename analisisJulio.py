# -*- coding: utf-8 -*-
"Criptoanalisis de Julio Cesar"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys
import hashlib

#Lee un archivo y retorna su hash en hexadecimal
def hashArchivo(archivo,metodo,bloque=1000):
	buf = archivo.read(bloque)
	while(buf!=""):
		metodo.update(buf)
		buf = archivo.read(bloque)
	return metodo.hexdigest()

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

def decifrar(cripto, k):
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

def imprimirTabla(d):
	tabla="TABLA DE FRECUENCIAS: \n"
	for n in range(0,len(vector),4):
		for i in range(4):
			tabla=tabla+vector[n+i]+": "+str(d[vector[n+i]])+"\t"
		tabla=tabla+"\n"
	return tabla

def obtenerClave(vector):
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
	print("23-Octubre-2014")

letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 'Ñ', "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
alfabeto=28
lineas=100

letrasPosicion={}
for n in range(alfabeto):
	letrasPosicion[letras[n]]=n

k=letrasPosicion.keys()
posicionLetras={}

for n in k:
	posicionLetras[letrasPosicion[n]]=n

frecuencias={}

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
	clave=obtenerClave(vector)
	if(clave==-1):
		print("No se puedo decifrar")
	else:	
		log=open(file+".log","w")
		log.write(imprimirTabla(frecuencias)+"\n")
		log.write("CLAVE: "+str(posicionLetras[clave]))
		log.close()

		file2=file+".dec"
		output=open(file2,"w")
		p=input.read(lineas)
		while(p!=""):
			output.write(decifrar(p,clave))
			p=input.read(lineas)
		input.close()
		output.close()
		md5=open(file+".MD5","w")
		md5.write(file+": ")
		md5.write(hashArchivo(open(file,"rb"),hashlib.md5()))
		md5.write("\n"+file2+": ")
		md5.write(hashArchivo(open(file2,"rb"),hashlib.md5()))
		md5.close()
		print("     Descifrado!")



	

