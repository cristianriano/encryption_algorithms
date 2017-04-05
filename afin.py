"Algoritmo Cryptografico de Cifrado Afin"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys
import base64
import hashlib
import os

def cifrar(frase):
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

def descifrar(crypto):
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

#Lee un archivo y retorna su hash en hexadecimal
def hashArchivo(archivo,metodo,bloque=1000):
	buf = archivo.read(bloque)
	while(buf!=""):
		metodo.update(buf)
		buf = archivo.read(bloque)
	return metodo.hexdigest()

def imprimirAyuda():
	print("afin.py es un programa para cifrar un archivo usando el algoritmo de cifrado")
	print("a fin, usando 2 parametros A y B. Ambos deben ser menores que 64 y ademas")
	print("A y 64 deben ser coprimos")
	print(" ")
	print("SINTAXIS:")
	print("python afin.py -cifrado_decifrado -e archivo_entrada -s archivo_salida -A numeroA -B numeroB")
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
	print("|python afin.py -c -e entrada.txt -s salida.cif -A 15 -B 3                   |")
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
	aIndex=0
	bIndex=0
	#Se obtienen los argumentos ingresados por el shell
	for n in range(0,len(sys.argv)):
		if(sys.argv[n]=="-e"):
			inIndex=n+1
		if(sys.argv[n]=="-s"):
			outIndex=n+1
		if(sys.argv[n]=="-A"):
			aIndex=n+1
		if(sys.argv[n]=="-B"):
			bIndex=n+1
	flag=False
	try:
		if(inIndex==0):
			raise NameError
		file=sys.argv[inIndex]
		input=open(file, "rb")
		if(aIndex==0 or bIndex==0):
			raise TypeError
		a=int(sys.argv[aIndex])
		b=int(sys.argv[bIndex])
		#Verificar condiciones de a y b para el algoritmo
		if(a>=alfabeto or b>=alfabeto):
			raise ZeroDivisionError
		if(MCD(alfabeto,a)!=1):
			raise ZeroDivisionError
		flag=True
	except ValueError:
		print("a y b deben ser numeros")
		imprimirAyuda()
	except ZeroDivisionError:
		print("a y b no cumplen con las condiciones")
		imprimirAyuda()
	except NameError:
		print("No hay archivo de entrada")
		imprimirAyuda()
	except TypeError:
		print("Ingrese los parametros a y b")
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
				output.write(cifrar(base64.b64encode(p)))
				p=input.read(72)
			input.close()
			output.close()
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
			inverso=calcularInverso(a,alfabeto)
			p=input.read(600)
			while(p!=""):
				tmp.write(descifrar(p))
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
