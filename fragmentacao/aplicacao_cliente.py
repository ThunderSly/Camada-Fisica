
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
# Carareto
# 17/02/2018
#  Aplicação
####################################################

print("comecou")

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
serialName = "COM6"                  # Windows(variacao de)


print("porta COM aberta com sucesso")


def main():
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    # verificar que a comunicação foi aberta
    print("comunicação aberta")

    # a seguir ha um exemplo de dados sendo carregado para transmissao
    # voce pode criar o seu carregando os dados de uma imagem. Tente descobrir
    # como fazer isso
    print("gerando dados para transmissao :")

    #txBuffer = b'BRUNAO 123456789'
    #txLen    = len(txBuffer)
    #print("Tamanho do arquivo enviado: " + str(txLen/1024) + " kb." )
    #print("Tempo estimado: " + str(((10*txLen*2)+10+9)/com.fisica.baudrate)+ " segundos.")
    msgType = 0
    # Transmite dado
    print("tentado sincronizar ....")
    # com.sendData(4,txBuffer)
    com.sendData(1)
    print("Mensagem tipo 1 enviada")
    while msgType != 2:
        rxBuffer, nRx, msgType, pkgTotal, pkgCurrent = com.getData(2)
        print("Recebida mensagem do tipo: " + str(msgType) + "Esperado tipo 2")
        if (msgType != 2):
            com.sendData(1)

    if msgType == 2:
        com.sendData(3)
        print("Mensagem tipo 3 enviada")
    
    while msgType != 4:
        rxBuffer, nRx, msgType, pkgTotal, pkgCurrent = com.getData(2)
        print("Recebida mensagem do tipo: " + str(msgType) + "Esperado tipo 4")
        if (msgType != 4):
            com.sendData(3)

    

    if msgType == 4:
        final_pkg=rxBuffer
        pkgCount = 1
        com.sendData(5)
        pkgRealTotal = pkgTotal
        while pkgCount < pkgRealTotal:
             
            rxBuffer, nRx, msgType, pkgTotal, pkgCurrent = com.getData(2)
            if (msgType == 4) & (pkgCurrent == pkgCount+1 )& (pkgTotal == pkgRealTotal):
                pkgCount +=1
                com.sendData(5)
                final_pkg += rxBuffer

            elif pkgCurrent != (pkgCount +1):
                com.sendData(8)
            else:
                com.sendData(6)
        print("ARQUIVO RECEBIDO COM SUCESSO:")
        print(")))))))))))))))))))))))))))))")
        print(final_pkg)
        print("Tamanho do arquivo recebido: " + str((len(final_pkg))/1024) + " kb.")
        # sucesso
        print(")))))))))))))))))))))))))))))")
        while msgType != 7:
            rxBuffer, nRx, msgType, pkgTotal, pkgCurrent = com.getData(2)
        print("-------------------------")
        print("Recebida mensagem tipo" + str(msgType)) 
        print("Tamanho do arquivo recebido: " + str(txLen/1024) + " kb.")
        print("Comunicação encerrada")
        print("-------------------------")
        com.disable()
    # Atualiza dados da transmissão
    txSize = com.tx.getStatus()


    # so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
