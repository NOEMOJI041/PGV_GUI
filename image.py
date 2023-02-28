import socket

ip = "192.168.2.2"
port = "50020"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, int(port)))
while True:
    req_data = bytes.fromhex('A8')
    checksum_data = bytes.fromhex('57')
    s.send(req_data)
    s.send(checksum_data)
    redhead_output = s.recv(2000).hex()
    print(redhead_output)

    D1 = bytes.fromhex("08")
    D2 = bytes.fromhex("E0")
    D3 = bytes.fromhex("00")
    D4 = bytes.fromhex("00")
    D5 = bytes.fromhex("00")
    D6 = bytes.fromhex("00")
    D7 = bytes.fromhex("00")
    D8 = bytes.fromhex("00")
    D9 = bytes.fromhex("E8")
    s.send(D1)
    s.send(D2)
    s.send(D3)
    s.send(D4)
    s.send(D5)
    s.send(D6)
    s.send(D7)
    s.send(D8)
    s.send(D9)

    redhead_output = s.recv(5000)
    print(redhead_output)

# Dz = bytes.fromhex("00")
# Dx = bytes.fromhex("FF")
# Dc = bytes.fromhex("FF")
# og1 = s.send(Dz)
# og2 = s.send(Dx)
# og3 = s.send(Dc)
# redhead_output = s.recv(2000).hex()
# print(redhead_output)


