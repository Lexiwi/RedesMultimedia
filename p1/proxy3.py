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
mu = (int(retMin)+int(retMax))/2
sigma = (mu+int(retMax))/3


class hilo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def calcula(self, data, sock):
        umbral = random.random()
        if(umbral > float(perdidas)):
            dormir = random.gauss(mu, sigma)
            while (dormir < float(retMin)) and (dormir > float(retMax)):
                dormir = random.gauss(mu, sigma)
            time.sleep(dormir/1000)
            sock.sendto(data, (addrDest, int(portDest)))


sockRecibir = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
sockRecibir.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, TAMANO_DEL_BUFFER)

sockEnviar = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

sockRecibir.bind((addrSrc, int(portSrc)))


while True:
    # Se pone el servidor a la escucha
    data, addr = sockRecibir.recvfrom(TAMANO_DEL_BUFFER)
    h = hilo()
    h.calcula(data, sockEnviar)
