# -*- coding: windows-1252 -*-
import socket
import time
import struct
import random
import sys

# Declaracion de variables 
IP = "150.244.65.81"
PORT = 5004
ESPERA = 10 #s
REPETICIONES = 5+1 # El primer paquete no se usa para la medida, pues suele falsear el resultado

sumaOffset = 0
offsetMin = sys.float_info.max
offsetMax = -sys.float_info.max
sumaRTT = 0
rttMin = sys.float_info.max
rttMax = -sys.float_info.max
numPaq = 0

print ("Direcci�n IP de destino:", IP)
print ("Puerto UDP de destino:", PORT)

   
# Se crea un socket
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
# Se fija un tiempo m�ximo de espera por si se perdiera alg�n paquete
sock.settimeout(ESPERA)

for i in range(0,REPETICIONES) :
	# Se duerme al programa para aleatorizar los tiempos entre sondeos
	if i>0: time.sleep(5*random.random())
	
	# Se coge el tiempo antes de enviar
	tenvio=time.time()
	# Se env�a el mensaje al destino
	sock.sendto(struct.pack("d",tenvio), (IP, PORT))

	try :
		# Se espera la respuesta
		data, addr = sock.recvfrom(2048)
		# Se toma el tiempo de recepci�n
		trecepcion = time.time()
	except :
		# Se cumpli� el tiempo m�ximo de espera, o el servidor no estaba escuchando y llegaron mensajes ICMP de puerto inalcanzable
		print ("Se perdi� alg�n paquete...")
		continue

	# El primer paquete suele dar medidas diferentes al resto, con lo que no se hace nada con �l
	if i>0 :
	
		# Se calcula el RTT
		rtt = trecepcion-tenvio
		# Se recoge el valor del tiempo en el servidor
		ts = struct.unpack("d",data)[0]
		# Se calcula el offset
		offset = ts - tenvio - rtt/2

		# Se revisa si el offset es mayor o menor que los anteriores
		if offset > offsetMax : offsetMax=offset
		if offset < offsetMin : offsetMin=offset
		# Se van sumando, para calcular luego la media
		sumaOffset += offset

		# Se revisa si el rtt es mayor o menor que los anteriores
		if rtt > rttMax : rttMax=rtt
		if rtt < rttMin : rttMin=rtt
		# Se van sumando, para calcular luego la media
		sumaRTT += rtt

		# Se entregan los resultados
		print ("Tiempo de env�o:", tenvio,"s")
		print ("Tiempo en el servidor:", ts,"s")
		print ("Tiempo de recepci�n:", trecepcion,"s")
		print ("RTT:", rtt,"s")
		print ("Offset:", offset,"s")
		print ()

		# Se incrementa el contador de paquetes v�lidos para la medida
		numPaq += 1
	
# Se calculan los valores medios	
offsetMedio=sumaOffset/numPaq
rttMedio=sumaRTT/numPaq

# Se imprimen los resultados generales de la medida
print("RTT m�nimo:",rttMin,"s")
print("RTT m�ximo:",rttMax,"s")
print("RTT medio:",rttMedio,"s")
print("Offset m�nimo:",offsetMin,"s")
print("Offset m�ximo:",offsetMax,"s")
print("Offset medio:",offsetMedio,"s")
print("Medida realizada sobre",numPaq,"paquetes")
print()
	
input("Pulse Enter para finalizar...")


