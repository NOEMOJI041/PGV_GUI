import io
import socket
from PIL import Image
from PIL import ImageFilter





ip = "192.168.2.2"
port = "50020"






s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, int(port)))


# s.send(b'\xa8'b'\x57')




s.send(b'\x08'b'\xe0'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\xe8')
while True:
    file_stream = io.BytesIO()
    redhead_output = s.recv(4096)

    while redhead_output:
        file_stream.write(redhead_output)
        redhead_output = s.recv(4096)

    image = Image.open(file_stream)
    image = image.filter(ImageFilter.GaussianBlur(radius = 10))

    image.save('fz.jpeg', format= 'JPEG')

with open('fz_ed.jpeg', 'wb') as file:
    redhead_output = s.recv(4096)

    while redhead_output:





# s.send(b'\x00'b'\xff'b'\xff')
