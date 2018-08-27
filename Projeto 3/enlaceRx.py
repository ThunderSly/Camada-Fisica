#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
# Carareto
# 17/02/2018
#  Camada de Enlace
####################################################

# Importa pacote de tempo
import time

# Threads
import threading

# Class


class RX(object):
    """ This class implements methods to handle the reception
        data over the p2p fox protocol
    """

    def __init__(self, fisica):
        """ Initializes the TX class
        """
        self.fisica = fisica
        self.buffer = bytes(bytearray())
        self.threadStop = False
        self.threadMutex = True
        self.READLEN = 1024
        self.eop = b'NAO'
        self.head = (0).to_bytes(10,byteorder="big")
        self.byte_stuff = b'BAIT'
        self.size_head = 0
        self.size_real = 0

    def thread(self):
        """ RX thread, to send data in parallel with the code
        essa é a funcao executada quando o thread é chamado.
        """
        while not self.threadStop:
            if(self.threadMutex):
                rxTemp, nRx = self.fisica.read(self.READLEN)
                if (nRx > 0):
                    self.buffer += rxTemp
                time.sleep(0.01)

    def threadStart(self):
        """ Starts RX thread (generate and run)
        """
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()

    def threadKill(self):
        """ Kill RX thread
        """
        self.threadStop = True

    def threadPause(self):
        """ Stops the RX thread to run

        This must be used when manipulating the Rx buffer
        """
        self.threadMutex = False

    def threadResume(self):
        """ Resume the RX thread (after suspended)
        """
        self.threadMutex = True

    def getIsEmpty(self):
        """ Return if the reception buffer is empty
        """
        if(self.getBufferLen() == 0):
            return(True)
        else:
            return(False)

    def getBufferLen(self):
        """ Return the total number of bytes in the reception buffer
        """
        return(len(self.buffer))

    def getAllBuffer(self, len):
        """ Read ALL reception buffer and clears it
        """
        self.threadPause()
        b = self.buffer[:]
        self.clearBuffer()
        self.threadResume()
        return(b)

    def getBuffer(self, nData):
        """ Remove n data from buffer
        """
        self.threadPause()
        b = self.buffer[0:nData]
        self.buffer = self.buffer[nData:]
        self.threadResume()
        return(b)

    def checkEop(self):
        a = self.buffer
        print(a.count(self.eop))
        print(a.count(self.byte_stuff))
        if (a.count(self.eop) > a.count(self.byte_stuff+self.eop)):
            return True
        else:
            return False

    def getNData(self):
        """ Read N bytes of data from the reception buffer

        This function blocks until the number of bytes is received
        """
#        temPraLer = self.getBufferLen()
#        print('leu %s ' + str(temPraLer) )

        # if self.getBufferLen() < size:
            # print("ERROS!!! TERIA DE LER %s E LEU APENAS %s", (size,temPraLer))
        while not(self.checkEop) or self.getBufferLen() == 0:
            print(self.getBufferLen())
            print(self.checkEop())
            time.sleep(0.1)
        self.buffer = self.getBuffer(self.getBufferLen())
        print(self.buffer)
        self.size_head = int.from_bytes(self.buffer[:10], byteorder='big')
        self.size_real = len(self.buffer)
        self.buffer = self.buffer[len(self.head):]
        lista_eops = []
        c = -1
        overhead = self.size_real/self.size_head
        throughput = overhead*self.fisica.baudrate
        print("Overhead: " +str(overhead))
        print("Throughput: " +str(throughput))
        while True:
            print(self.buffer)
            c = self.buffer.find(self.eop, c+1)
            print(c)
            if c == -1:
                print("Nao tme eop")
                break
            else:
                print("Posição do eop bait: " + str(c))
                lista_eops.append(c)
        print(lista_eops)
        if len(lista_eops)>0:
            for i in lista_eops:
                self.buffer = self.buffer[:i] + self.buffer[i+len(self.byte_stuff):]
            print(self.buffer)
        
        if self.buffer.find(self.eop)!=-1:
            print("Posição de início de EOP: " +str(self.buffer.find(self.eop)))

        elif self.buffer.find(self.eop)==-1:
            print("ERRO NÃO HÁ EOP")

        self.buffer = self.buffer[:-len(self.eop)]
        print(len(self.buffer))
        print(self.size_head)
        if len(self.buffer) != self.size_head:
            print("ERRO TAMANHO INCOMPATIVEL")      
        return (self.buffer)



    def clearBuffer(self):
        """ Clear the reception buffer
        """
        self.buffer = b""


