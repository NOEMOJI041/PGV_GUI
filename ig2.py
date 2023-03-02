import socket
import struct
address = ("192.168.2.2", 50020)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)




buf = ''
# s.send(b'\x00'b'\xff'b'\xff')
s.send(b'\xa8'b'\x57')

while len(buf)<4:
    s.send(b'\x08'b'\xe0'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\xe8')

    buf += s.recv(4-len(buf))
size = struct.unpack('!i', buf)
print ("receiving %s bytes" % size)

with open('tst.jpg', 'wb') as img:
    while True:
        data = s.recv(1024)
        if not data:
            break
        img.write(data)
print ('received, yay!')

s.close()
