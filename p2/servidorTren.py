######################
#	servidorTren.py  #
#	Prácticas RM     #
######################


import sys
import socket
import struct
import time

MAX_ETHERNET_DATA=1500
MIN_ETHERNET_DATA=46
ETH_HDR_SIZE=14+4+8 # MAC header + CRC + Preamble
IP_HDR_SIZE=20
UDP_HDR_SIZE=8
RTP_HDR_SIZE=12

MAX_WAIT_TIME=8
MAX_BUFFER=100000000

packet_list=[]
B_MASK=0xFFFFFFFF
DECENASMICROSECS=100000

#Lista de tiempos de llegada
list_llegada = []
#Lista de retardos
list_retardo = []
#Lista de ancho de banda
list_AB = []


if __name__ == "__main__":
	if len(sys.argv)!=3:
		print ('Error en los argumentos:\npython servidorTren.py ip_escucha puerto_escucha\n')
		exit(-1)

	ipListen=sys.argv[1]
	portListen=int(sys.argv[2])
	sock_listen = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
	sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF,MAX_BUFFER)
	sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock_listen.bind((ipListen,portListen))
	sock_listen.settimeout(MAX_WAIT_TIME)
	
	#Recibimos los paquetes y salimos del bucle cuando no se reciban paquetes en MAX_WAIT_TIME segundos
	while True:
		try:
			data, addr = sock_listen.recvfrom(2048)
			#Para cada paquete recibido añadimos a la lista de paquetes
			#una tupla que contiene los datos del paquete y el tiempo en que 
			#se recibió dicho paquete
			packet_list.append((data,time.time()))

		except socket.timeout:
			break
	npackets=0
	
        #Lista de tiempos de llegada
        tms_llegada = []
        #Lista de retardos
        tms_retardos=[]
        #Lista de ancho de banda
	list_AB = []

	for packet in packet_list:
		#Para cada paquete recibido extraemos de la cabecera
		#cada uno de los campos necesarios para hacer los cálculos
		
		data=packet[0]
		header=struct.unpack('!HHII',data[0:12])
		seq_number=header[1]
		send_time_trunc=header[2]
		trainLength=header[3]
		#ATENCIÓN: El tiempo de recepción está en formato: segundos.microsegundos
		#Usar este tiempo para calcular los anchos de banda
		reception_time=packet[1]
		npackets+=1 #Media
		#Truncamos el tiempo de recepción a centésimas de milisegundos 
		#(o decenas de microsegundos, segun se quiera ver) y 32 bits
		#para poder calcular el OWD en la misma base en que está eñ tiempo
		#de envío del paquete
		reception_time_trunc=int(reception_time*DECENASMICROSECS)&B_MASK
		
		print ('Retardo instantaneo en un sentido (s): ',(reception_time_trunc-send_time_trunc)/DECENASMICROSECS)

		
		###########################PRÁCTICA##############################################
		#                                                                               #
		# Añadir cálculos necesarios para obtener ancho de banda (instantáneo,medio,    #
		# máximo,mínimo) y retardo en un sentido (instantáneo, medio, máximo y mínimo)  #
		# ATENCIÓN: los tiempos truncados están en centésimas de milisegundos           # 
		#         (o decenas de microsegundos, segun se quiera ver)                     #
		# a la hora de calcular retardos se debe tener en cuenta                        #
		#################################################################################

                #Guardamos en list_llegada el tiempo truncado del paquete(segundos.microsegundos)
                list_llegada.append(reception_time)

                #Podemos calcular el ancho de banda a partir del segundo paquete recibido
                if (npackets > 1):
                    #Tamanio total a medir
                    tamTotal = (len(data)+cab)*8
                    #Calculamos el ancho de banda instantaneo
                    ABInstantaneo = tamTotal / (list_llegada[-1] - list_llegada[-2])
                    #Anyadimos el ancho de banda calculado a la lista de ancho de bandas
                    list_AB.append(ABInstantaneo)
                    print ('Ancho de banda instantaneo: ',ABInstantaneo)

                #Guardamos en la lista el retardo del paquete
                retardoInstantaneo = (reception_time_trunc - send_time_trunc)/DECENASMICROSECS
                list_retardo.append(retardoInstantaneo)
                print ('Retardo instantaneo: ', retardoInstantaneo)


        #Calculamos el retardo y ancho de banda medio del tren
        AB_medio = (npackets - 1)*tamTotal / sum(list_AB)
        retardo_medio = sum(list_retardo) / npackets

        print('Ancho de banda medio: ', AB_medio)
        print('Ancho de banda maximo: ', max(list_AB))
        print('Ancho de banda minimo: ', min(list_AB))

	print ('Retardo medio en un sentido : ', retardo_medio)
	print ('Retardo maximo en un sentido : ', max(list_retardos))
	print ('Retardo minimo en un sentido : ', min(list_retardos))
	
	###########################PRÁCTICA##############################################
	#                                                                               #
	# Añadir cálculos necesarios para obtener pérdida de paquetes y variación del   #
	# retardo                                                                       #
	#################################################################################
        #ME QUEDE AQUI
	packetLoss=0
	print('Perdida de paquetes: ',packetLoss)
	jitter=0 
	print('Variación del retardo: ',jitter)
	#################################################################################




