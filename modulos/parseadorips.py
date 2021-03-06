from modulos.geo import geolo
from modulos.loading import Spinner

try:
    from scapy.all import *
    from modulos import geo
except:
    print("Instala scapy o verifica el git.")


def parseador():
    pkts = rdpcap('logs')
    dic = {}
    dic2 = {}
    contador = 0
    for pkt in pkts:
        temp = pkt.sprintf("%IP.dst%")
        dic[temp] = "1"

    for a in dic.keys():
        contador += 1
        dic2[contador] = a
    i = 1

    print("===========================================")
    for i in dic2:
        try:
            with Spinner():
                print(dic2[i] + " {}".format(geo.geolo(dic2[i])))
        except:
            pass
    print("===========================================")

    opc = input("¿Necesitas un archivo de esto? [y/n] ==> ")
    if opc == 'y':
        nombre = input("¿Qué nombre le quieres poner? ==> ")
        with open("Data\\" + nombre+'.txt', 'w') as f:
            f.write("Estas son las IPS que encontre: \n")
            for i in dic2:
                try:
                    f.write(dic2[i] + " " + (geolo(dic2[i])) + "\n")
                except:
                    pass

        print("IPs guardadas correctamente :D")
    else:
        print("Hasta la proxima")


