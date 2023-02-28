import socket


class Client:
    def __init__(self):
        self.ip = "192.168.2.2"
        self.port = "50020"
        self.req_data = 0
        self.checksum_data = 0
        self.redhead_output = 0
        self.conn()

    def conn(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, int(self.port)))

        while True:
            self.req_data = bytes.fromhex('D0')
            self.checksum_data = bytes.fromhex('2F')
            s.send(self.req_data)
            s.send(self.checksum_data)
            self.redhead_output = s.recv(61).hex()
            return self.redhead_output


