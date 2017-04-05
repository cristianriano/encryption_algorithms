
import sys

def cifrarTransDoble(frase):
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

def desTransDoble(crypto):
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

def imprimirAyuda():
	print("transDoble es un programa para codificar un archivo de texto")
	print("usando el algoritmo de transposicion doble")
	print(" ")
	print("SINTAXIS:")
	print("python transDoble.py -parametro archivo_entrada archivo_salida")
	print("-----------------------------------------------------------------------------")
	print("|PARAMETROS:                                                                 |")
	print("|-c	Para cifrar                                                         |")
	print("|-d	Para descifrar                                                      |")
	print("|-a	Para ayuda                                                          |")
	print("|                                                                            |")
	print("|EJEMPLO:                                                                    |")
	print("|python transDoble.py -c entrada.txt salida.cif                              |")
	print("-----------------------------------------------------------------------------")

if len(sys.argv)<=1:
	print("Escriba transDoble -a para obtener ayuda")

else:
	parametro=sys.argv[1]
	if (parametro=="-a"):
		
	else:	
		try:
			file=sys.argv[2]
			input=open(file, "r")
		except:
			print("No se pudo abrir el archivo de entrada")
	
	
		if (parametro=="-c"):
			try:
				file2=sys.argv[3]
				if("." in file2):
					file2=file2+".cif"
				output=open(file2, "a")
			except:
				print("No se pudo abrir el archivo de salida")
			for line in input:
				if line[len(line)-1]=="\n":
					line=line[:len(line)-1]
				output.write(cifrarTransDoble(line)+"\n")
			input.close()
			output.close()
	
		elif(parametro=="-d"):
			try:
				file2=sys.argv[3]
				if("." in file2):
					file2=file2+".dec"
				output=open(file2, "a")
			except:
				print("No se pudo abrir el archivo de salida")
			for line in input:
				if line[len(line)-1]=="\n":
					line=line[:len(line)-1]
				output.write(desTransDoble(line)+"\n")
			input.close()
			output.close()
		else:
			imprimirAyuda()
