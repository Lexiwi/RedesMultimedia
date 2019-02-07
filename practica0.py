import struct
import threading
import time
import socket

IP = "127.0.0.1"
PORT = 5004

class hilo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.seguir=True

    def run(self):
        self.abrirServidor()

    def abrirServidor(self):
        # Se crea un socket para recibir (servidor)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.bind((IP, PORT))
        while self.seguir == True:
            # Se pone el servidor a la escucha
            data, addr = sock.recvfrom(2048) # Tamanio del buffer de recepcion
            print(time.strftime("%x %X", time.gmtime())," <",addr,">: ")
            print(data.decode())
            print("\n")

    def parar(self):
        self.seguir=False


#Inicializamos el hilo
h = hilo()
#Llamando a este metodo inciamos la ejecucion del hilo y se ejecuta el codigo contenido en el metodo run
h.start()

ipDest = input("Introduce IP del destinatario: ")
portDest = input("Introduce puerto del destinatario: ")

# Se crea un socket
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

salida = True
sqnum = 1
while(salida):
    msg = input()

    if msg == "{quit}":
        salida = False

    else:
        cabecera = struct.pack('!HHII',0x8014,sqnum, int(time.time()),0)
        sqnum += 1
        mensaje = str.encode(msg)
        sock.sendto(cabecera + mensaje, (ipDest, int(portDest)))


#Llamando a este metodo le decimos a la clase hilo que pare su ejecucin
h.parar()
#Con esta instruccion esperamos a que acabe el hilo
h.join()
