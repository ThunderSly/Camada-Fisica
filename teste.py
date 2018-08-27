buffer = bytes(bytearray())
eop = b'NAO'
byte_stuff = b'BAIT'
buffer = b'BRU123456789NAOgfbfgbgbfg NAO 123456789 yjyjyjyj'
lista_eops = []
c = -1
buffer_stuff = buffer
while True:
    print(buffer)
    c = buffer.find(eop, c+1)
    print(c)
    if c == -1:
        print("Nao tme eop")
        break
    else:
        print("Posição do eop bait: " + str(c))
        lista_eops.append(c)
print(lista_eops)
if len(lista_eops) > 0:
    k = 0
    for i in lista_eops:
        buffer_stuff = buffer_stuff[:i+k] + byte_stuff + buffer_stuff[k+i:]
        k += len(byte_stuff)
        print(buffer_stuff)
for i in lista_eops:
    buffer_stuff = buffer_stuff[:i] + buffer_stuff[i+len(byte_stuff):]
print(buffer_stuff)

