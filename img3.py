import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.2.2", 50020))

bs = 4096


with open('txp.txt', 'w') as file:
    client.send(b'\x08'b'\xe0'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\xe8')
    recv_data = client.recv(bs).hex()

    while recv_data:
        file.write(recv_data)
        recv_data = client.recv(bs).hex()