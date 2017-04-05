"Algoritmo Cryptografico de Transposicion por Grupos"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
import sys

def cifrarTransGrupos(frase, llave):
	cryptograma=''
	for m in llave:
		cryptograma=cryptograma+frase[m-1]		
	return cryptograma

def stuff(frase, llave):
	grupo=len(llave)
	relleno=grupo-(len(frase)%grupo)
	if(relleno==grupo):
		relleno=0
	for n in range(relleno):
		frase=frase+"#"
	return frase

def unstuff(cola,llave):
	cut=0
	for n in range(len(cola),0,-1):
		if(cola[n-1]!="#"):
			break
		else:
			cut=n
	cola=cola[:cut-1]
	return cola

def desTransGrupos(crypto, llave):
	mensaje=""
	grupo=len(llave)
	bloque1=[""]
	for n in range(1,grupo):
		bloque1.append("")
	for m in range(grupo):
		try:
			bloque1[llave[m]-1]=crypto[m]
		except:
			pass
	mensaje=mensaje+("".join(bloque1))
	return mensaje

def verificarClave(llave):
	tmp=sorted(llave)
	for n in range(len(llave)):
		if(not(tmp[n].isdigit())):
			print("La clave no es numerica")
			return False
		if(not(int(tmp[n])==n+1)):
			print("No es una clave valida")
			return False
	return True
	
def imprimirAyuda():
	print("transGrupos.py es un programa para codificar un archivo usando el algoritmo")
	print("de transposicion por grupos definiendo una llave")
	print(" ")
	print("SINTAXIS:")
	print("python transSimple.py -parametro -k clave -e archivo_entrada -s archivo_salida")
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
	print("|python transSimple.py -c -k clave.txt -e entrada.txt -s salida.cif          |")
	print("|                                                                            |")
	print("|SINTAXIS CLAVE:                                                             |")
	print("|    5,3,1,2,4                                                               |")
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
	claveIndex=0
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
			raise ValueError
		if(claveIndex==0):
			raise NameError
		file=sys.argv[inIndex]
		input=open(file, "rb")
		file3=sys.argv[claveIndex]
		clave1=open(file3, "rb")
		clave=[]
		claves=(clave1.read()).replace(" ","")
		claves=claves.replace("\n","")
		clave=claves.split(",")
		flag2=False
		flag2=verificarClave(clave)
		if(flag2):
			for n in range(len(clave)):
				clave[n]=int(clave[n])
		flag=True
	except ValueError:
		print("No hay archivo de entrada")
	except NameError:
		print("Ingrese una llave para realizar proceso")
	except:
		if(flag2):
			print("No se pudo abrir el archivo de entrada")	
	if (parametro=="-c" and flag and flag2):
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
			t=len(clave)
			p=input.read(t)
			while(len(p)==t):
				output.write(cifrarTransGrupos(p, clave))
				p=input.read(t)
			if(len(p)>0):
				output.write(cifrarTransGrupos(stuff(p,clave), clave))
			input.close()
			output.close()
		except:
			print("No se pudo abrir el archivo de salida")
		
	
	elif(parametro=="-d" and flag and flag2):
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
			t=len(clave)
			p=input.read(t)
			while(True):
				q=input.read(t)
				if(q!=""):
					output.write(desTransGrupos(p, clave))
					p=q
				else:
					break
			if(len(p)>0):
				q=desTransGrupos(p,clave)
				output.write(unstuff(q,clave))
			input.close()
			output.close()
		except:
			print("No se pudo abrir el archivo de salida")
	elif(flag2):		
		imprimirAyuda()
