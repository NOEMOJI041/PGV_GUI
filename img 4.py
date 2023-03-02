import socket
from PIL import Image
import io

class Client:
    def __init__(self):
        self.ip = "192.168.2.2"
        self.port = "50020"
        self.req_data = 0
        self.checksum_data = 0
        self.redhead_output = 0
        self.s = 0
        self.a = 0
        self.conn()


    def conn(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, int(self.port)))
        # self.s.send(b'\xa8'b'\x57')
    def output(self):

        self.s.send(b'\x08'b'\xe0'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\xe8')
        a = ''
        self.redhead_output = self.s.recv(4).hex()
        while True:
            self.redhead_output = self.s.recv(4).hex()
            print(self.redhead_output)
            a = self.redhead_output + a
            if self.redhead_output == "7fe0":
                break

        print(len(a))


if __name__ == "__main__":
    cs = Client()
    cs.output()