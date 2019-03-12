# -*- coding: windows-1252 -*-
import socket
import time
import struct

# Declaraci�n de variables  
IP_SERVER = "150.244.66.53"
PORT_SERVER = 5004
ESPERA = 60


print ("Direcci�n IP de escucha:", IP_SERVER)
print ("Puerto UDP de escucha:", PORT_SERVER)


# Se crea un socket para recibir (servidor)
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

sock.bind((IP_SERVER, PORT_SERVER))
sock.settimeout(ESPERA)


while True:
	try :
		# Se pone el servidor a la escucha
		data, addr = sock.recvfrom(2048) # Tama�o del buffer de recepci�n

		ts=time.time()
		# Se env�a de vuelta el tiempo al recibir
		sock.sendto(struct.pack("d",ts), addr)
		
	except :
		print("Se cumpli� el tiempo m�ximo de espera sin recibir paquetes")
		break