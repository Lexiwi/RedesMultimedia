#!/bin/bash
#########################################
#Este script cambia la configuracion de #
#las interfaces de los laboratorios para#
#negociar la velocidad a 10Mbps y 	#
#los parametros de offloading y 	#
#moderacion de RX y TX			#
#Practicas RM 2014-2015			#
#Uso: ./changeParameters.sh		#
#########################################
sudo ethtool -s  eth0 speed 10 duplex full
sudo ethtool -K eth0 gso off
sudo ethtool -K eth0 gro off
sudo ethtool -K eth0 lro off
sudo ethtool -A eth0 rx off
sudo ethtool -A eth0 tx off

