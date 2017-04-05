"Algoritmo Cryptografico de Transposicion por Series"
"Cristian Camilo Riano	cristianriano@unicauca.edu.co"
"Diego Alejandro Alvis	diegoalvis@unicauca.edu.co"
"9256...3ae0"

import sys

def cifrar(frase, serie):
	cryptograma=''
	for n in serie:
		cryptograma=cryptograma+frase[n-1]
	return cryptograma
	
def stuff(frase, serie):
	stuf=len(serie)-(len(frase)%len(serie))
	if(stuf==len(serie)):
		stuf=0
	for n in range(stuf):
		frase=frase+"#"
	return frase
	
def descifrar(crypto, serie):
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

def obtenerSerie(funciones):
	serie=[]
	for n in range(len(funciones)):
		for m in range(len(funciones[n])):
			serie.append(funciones[n][m])
	return serie

def imprimirAyuda():
	print("transSeries.py es un programa para codificar un archivo usando el algoritmo")
	print("de transposicion por series")
	print(" ")
	print("SINTAXIS:")
	print("python transSeries.py -parametro -e archivo_entrada -k archivo_claves -s archivo_salida")
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
	print("|python transSeries.py -c -e entrada.txt -k clave.txt -s salida.cif                       |")
	print("-----------------------------------------------------------------------------")
	print(" ")
	print("AUTORES: ")
	print("Cristian Camilo Riano	cristianriano@unicauca.edu.co")
	print("Diego Alejandro Alvis	diegoalvis@unicauca.edu.co")

def imprimirAyudaClave():
	print("")
	print("*El archivo clave de contener unicamente numeros")
	print("*Los elementos de cada funcion deben estar separados por coma (,)")
	print("*En el archivo deben estar todos los numeros desde 1 al mayor valor de la clave")
	print("EJEMPLO SINTAXIS PARA ARCHIVO ")
	print("1,3,5")
	print("2,8")
	print("6,4,7")
	print("-----------------------------------------------------------------------------")
	
if len(sys.argv)<2:
	imprimirAyuda()
elif sys.argv[1]=="-a":
	imprimirAyuda()
else:
	parametro=sys.argv[1]
	inIndex=0
	outIndex=0
	funIndex=0
	for n in range(0,len(sys.argv)):
		if(sys.argv[n]=="-e"):
			inIndex=n+1
		if(sys.argv[n]=="-s"):
			outIndex=n+1
		if(sys.argv[n]=="-k"):
			funIndex=n+1
	pola=False
	try:	
		if(inIndex==0):
			raise ValueError
		if(funIndex==0):
			raise NameError
	
		file=sys.argv[inIndex]
		file2=sys.argv[funIndex]
		input2=open(file2,"rb")
		input1=open(file, "rb")
		funciones=[]
		for line in input2: 
				line=line.replace("\n","") 
				line=line.replace(" ","") 
				funcion=line.split(",") 
				funciones.append(funcion)
		
		series=obtenerSerie(funciones)
		cl_order=sorted(series)
		cl_set=set(cl_order)
		for i in range(0,len(cl_order)):
			if(not(str(cl_order[i]).isdigit)):
				raise OSError

		if(len(cl_set)<len(cl_order)):
			raise TypeError 

		if(int(cl_order[len(cl_order)-1])>len(cl_set)):
			raise IOError 

		for i in range(0,len(series)):
			series[i]=int(series[i])
		size=len(input1.read())
		input1.close()
		input=open(file, "rb")
		pola=True

	except IOError:
		print("Faltan numeros en el archivo clave")
		imprimirAyudaClave()
	except TypeError:
		print("Hay numeros repetidos en el archivo clave")
		imprimirAyudaClave()
	except OSError:
		print("Lo elementos de la clave deben ser numericos unicamente")
		imprimirAyudaClave()
	except ValueError:
		print("No hay archivo de entrada")
		imprimirAyudaClave()
	except NameError:
		print("No hay archivo de clave")
		imprimirAyudaClave()
	except:
		print("No se pudo abrir el archivo de entrada")
	
	if (parametro=="-c" and pola):
		try:
			if outIndex==0:
				file3=file
				if("." in file):
					file3=file[:file.index(".")]
			else:
				file3=sys.argv[outIndex]
			if(not ("." in file3)):
				file3=file3+".cif"
			output=open(file3, "w") 
			p=input.read(len(series))
			while(len(p)==len(series)):
				output.write(cifrar(p,series))
				p=input.read(len(series))
			if(len(p)>0):
				output.write(cifrar(stuff(p,series),series))
			input.close()
			output.close()
		except: 
			print("No se pudo abrir el archivo de salida")

	if (parametro=="-d" and pola):
		try:
			if outIndex==0:
				file3=file
				if("." in file):
					file3=file[:file.index(".")]
			else:
				file3=sys.argv[outIndex]
			if(not ("." in file3)):
				file3=file3+".dec"
			output=open(file3, "w") 
			for n in range(0,size,72):
				output.write(descifrar(input.read(72),series))
			input.close()
			output.close()
		except: 
			print("No se pudo abrir el archivo de salida")




