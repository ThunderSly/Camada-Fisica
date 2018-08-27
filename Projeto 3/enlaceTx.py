#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Camada de Enlace
####################################################

# Importa pacote de tempo
import time

# Threads
import threading
    
# Class
class TX(object):
    """ This class implements methods to handle the transmission
        data over the p2p fox protocol
    """

    def __init__(self, fisica):
        """ Initializes the TX class
        """
        self.fisica      = fisica
        self.buffer      = bytes(bytearray())
        self.transLen    = 0
        self.empty       = True
        self.threadMutex = False
        self.threadStop  = False
        self.head = 0
        self.eop = b'NAO'
        self.byte_stuff= b'BAIT'

    def thread(self):
        """ TX thread, to send data in parallel with the code
        """

        while not self.threadStop:
            if(self.threadMutex):
                start_time = time.time()
                self.transLen    = self.fisica.write(self.buffer)
                print("O tamanho transmitido. Impressao dentro do thread {}" .format(self.transLen))
                elapsed_time = time.time() - start_time
                print("Tempo de envio: " + str(elapsed_time) + " segundos.")
                self.threadMutex = False

    def threadStart(self):
        """ Starts TX thread (generate and run)
        """
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()

    def threadKill(self):
        """ Kill TX thread
        """
        self.threadStop = True

    def threadPause(self):
        """ Stops the TX thread to run

        This must be used when manipulating the tx buffer
        """
        self.threadMutex = False

    def threadResume(self):
        """ Resume the TX thread (after suspended)
        """
        self.threadMutex = True

    def sendBuffer(self, data):
        """ Write a new data to the transmission buffer.
            This function is non blocked.

        This function must be called only after the end
        of transmission, this erase all content of the buffer
        in order to save the new value.
        """
        self.transLen   = 0
        self.buffer = data
        tamanho = len(self.buffer)
        print(tamanho)
        self.head = (tamanho).to_bytes(10,byteorder="big")
        print(self.head)
        print("EOP:" +str(self.eop))
        lista_eops=[]
        c=-1
        buffer_stuff = self.buffer
        while True:
            print(self.buffer)
            c = self.buffer.find(self.eop, c+1)
            print(c)
            if c == -1:
                print("Nao tem eop")
                break
            else:
                print("Posição do eop bait: "+ str(c))
                lista_eops.append(c)
            print(lista_eops)
        if len(lista_eops)>0:
            k=0
            for i in lista_eops:
                buffer_stuff = buffer_stuff[:i+k] + self.byte_stuff + buffer_stuff[k+i:]
                k += len(self.byte_stuff)
        print(buffer_stuff)      
        self.buffer = self.head + buffer_stuff + self.eop
        print(self.buffer)        
        self.threadMutex  = True

    def getBufferLen(self):
        """ Return the total size of bytes in the TX buffer
        """
        return(len(self.buffer))

    def getStatus(self):
        """ Return the last transmission size
        """
        #print("O tamanho transmitido. Impressao fora do thread {}" .format(self.transLen))
        return(self.transLen)
        

    def getIsBussy(self):
        """ Return true if a transmission is ongoing
        """
        return(self.threadMutex)

