import socket
from PIL import Image

HOST = "192.168.2.2"
PORT = 50020
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.send(b'\x08\xe0\x00\x00\x00\x00\x00\x00\x00\x00\xe8')
z = b''
data = client_socket.recv(1024)
print(data)
while True:
    client_socket.settimeout(2)
    try:
        data = client_socket.recv(1024)
    except:
        break
    z = z + data

b = bytearray(z)
del b[-1:]
a = bytes(b)
hex_img = a.hex()

bmp_bytes = bytes.fromhex(str(hex_img))
final_img = Image.frombytes("L", (376, 240), bmp_bytes)

final_img.show()