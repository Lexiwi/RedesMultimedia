import struct
import threading
import time

IP = "127.0.0.1"
PORT = 5004

class hilo(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.seguir=True

    def run(self):
        self.abrirServidor()
        self.escuchar()

    def abrirServidor(self):
	       # Se crea un socket para recibir (servidor)
           sock = socket.socket(socket.AF_INET, # Internet
                                   socket.SOCK_DGRAM) # UDP
           sock.bind((IP, PORT))

    def escuchar(self):
        while self.seguir == True:
        	# Se pone el servidor a la escucha
        	data, addr = sock.recvfrom(2048) # Tamanio del buffer de recepcion
        	print (time.strftime("%x %X", time.gmtime())," <",addr,">:)
        	print (data.decode())
            print ("\n")

        	# Se envia de vuelta el mismo contenido
        	sock.sendto(data, addr)

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
while(salida):
    msg = input()

    if msg == "{quit}"
        salida = False

    sock.sendto(msg.str.encode(), (ipDest, portDest))


#Llamando a este metodo le decimos a la clase hilo que pare su ejecucin
h.parar()
#Con esta instruccion esperamos a que acabe el hilo
h.join()
