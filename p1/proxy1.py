import threading
import time
import socket
import sys
import random

TAMANO_DEL_BUFFER = 100000

addrSrc = sys.argv[1]
portSrc = sys.argv[2]
addrDest = sys.argv[3]
portDest = sys.argv[4]
perdidas = sys.argv[5]
retMin = sys.argv[6]
retMax = sys.argv[7]

sockRecibir = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
sockRecibir.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, TAMANO_DEL_BUFFER)

sockEnviar = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

sockRecibir.bind((addrSrc, int(portSrc)))


while True:
    # Se pone el servidor a la escucha
    data, addr = sockRecibir.recvfrom(TAMANO_DEL_BUFFER)
    umbral = random.random()
    if(umbral > float(perdidas)):
        time.sleep((random.randrange(float(retMin), float(retMax)))/1000)
        sockEnviar.sendto(data, (addrDest, int(portDest)))
