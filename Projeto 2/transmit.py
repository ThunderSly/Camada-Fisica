
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
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

#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM4"                  # Windows(variacao de)



print("porta COM aberta com sucesso")



def main(filename):
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()


    #verificar que a comunicação foi aberta
    print("comunicação aberta")


    # a seguir ha um exemplo de dados sendo carregado para transmissao
    # voce pode criar o seu carregando os dados de uma imagem. Tente descobrir
    #como fazer isso
    print ("gerando dados para transmissao :")
  
   
    with open(filename, "rb") as imageFile:
        f = imageFile.read()


    txBuffer = bytes(f)
    txLen    = len(txBuffer)
    print("Tamanho do arquivo enviado: " + str(txLen/1024) + " kb." )
    print("Tempo estimado: " + str((txLen*10*2)/com.fisica.baudrate)+ " segundos.")

    # Transmite dado
    print("tentado transmitir ....")
    com.sendData(txBuffer)
    start_time = time.time()

        
    # Atualiza dados da transmissão
    txSize = com.tx.getStatus()



    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()

    elapsed_time = time.time() - start_time
    print("Tempo de envio: " + str(elapsed_time) + " segundos.")
    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
