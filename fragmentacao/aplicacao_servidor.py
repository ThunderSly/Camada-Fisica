#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
# Carareto
# 17/02/2018
#  Aplicação
####################################################

print("comecou")
import math
from enlace import *
import time


# voce deverá descomentar e configurar a porta com através da qual ira fazer a
# comunicaçao
# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

# serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
# serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM5"                  # Windows(variacao de)


print("porta COM aberta com sucesso")


def main():
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()
    # Faz a recepção dos dados
    txBuffer = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure'
    txLen = len(txBuffer)
    bufferlen = 128
    numberOfPackagesint = txLen // bufferlen
    numberOfPackages = math.ceil(txLen / bufferlen)
    list_pkg = []
    for i in range(0,numberOfPackagesint):
        list_pkg.append(txBuffer[i*bufferlen:(i+1)*bufferlen])
    list_pkg.append(txBuffer[numberOfPackagesint*bufferlen:])
    #print(list_pkg)
    #print(len(list_pkg))

    print("Tamanho do arquivo enviado: " + str(txLen/1024) + " kb.")
    print("Tempo estimado: " + str(((10*txLen*2)+10+9) /
                                   com.fisica.baudrate) + " segundos.")

    print("Esperando sincronização ....")
    rxBuffer, nRx, msgType, pkgTotal, pkgCurrent = com.getData()
    print(msgType)

    if msgType == 1:
        print("Comunicação começada (TIPO 1 RECEBIDO)")
        com.sendData(2)
        print(" TIPO 2 ENVIADO")
        while msgType != 3:
            rxBuffer, nRx, msgType, pkgTotal, pkgCurrent = com.getData(2)
            print("Recebida mensagem do tipo: " +
                  str(msgType) + "Esperado tipo 3")
        if msgType == 3:
            print("-------------------------")
            print("Handshake completo ")
            print(msgType)
            print("-------------------------")
            #com.sendData(4, txBuffer)
            time.sleep(0.5)


            pkg_success_count = 0
            while pkg_success_count < numberOfPackages:
                com.sendData(4, list_pkg[pkg_success_count], len(list_pkg), pkg_success_count + 1)
                rxBuffer, nRx, msgType, pkgTotal, pkgCurrent = com.getData(2)
                if msgType == 5:
                    pkg_success_count +=1
                if msgType == 6:
                    print("XXXXXXXXXXX PACOTE COM ERRO")
                    print("Falha no envio")
                if msgType == 8:
                    print("XXXXXXXXXXX PACOTE NUMERO ERRADO")
                    print("Falha no envio")
            print(")))))))))))))))))))))))))))))")
            print("Arquivo enviado e recebido com sucesso!")
            print(")))))))))))))))))))))))))))))")
            print("Enviando mensagem de encerramento")
            com.sendData(7)
            print("-------------------------")
            print("Comunicação encerrada")
            print("-------------------------")
            com.disable()

        else:
            print("Não foi recebida a mensagem do tipo 3")

    else:
        print("foi recebida uma msg de tipo:" + str(msgType))

    #rxBuffer, nRx, msgType, pkgTotal, pkgCurrent = com.getData()



    # Encerra comunicação
    # so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
