import socket
import io
from PIL import Image


class Client:
    def __init__(self):
        self.ip = "192.168.2.2"
        self.port = "50020"
        self.redhead_output = 0
        self.s = 0
        self.by = ''
        self.data = 0
        self.conn()

    def conn(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.s.settimeout(10)

        self.s.connect((self.ip, int(self.port)))
        self.s.send(b'\x08\xe0\x00\x00\x00\x00\x00\x00\x00\x00\xe8')
        self.data = (self.s.recv(100))


    def output(self):
        img = ''
        while True:
            data = self.s.recv(1024).hex()
            print(len(data))
            img += data
            print(data)
            with open("hex.txt", 'w') as file:
                file.write(img)
            # if len(data) < 300:
            #     break
        # dataBytesIO = io.BytesIO(img)
        # ok = dataBytesIO.seek(0)
        # image = Image.open(ok)
        # image.show()
        # t_img = io.BytesIO(img)
        # t_img = t_img.seek(0)
        # img = Image.open(t_img)
        # # img.save()
        # img.show()
        # cCode = img.getcolors(256)
        # cCode = str(cCode)
        # print(cCode)

    def recvall(self):

        BUFF_SIZE = 4096  # 4 KiB
        data = b''
        while True:
            part = self.s.recv(BUFF_SIZE)
            print(len(part))
            data += part
            # if len(part) < BUFF_SIZE:
                # either 0 or end of data
                # break
            print(part)

            if len(data) == 1:
                break
        print(data)

            # # print(self.redhead_output)
            # # with open("ok.txt", 'a') as file:
            # #     file.write(str(self.redhead_output))
            # #     file.flush()
            # # if len(self.redhead_output) < 400:
            # #     break
            # # self.by = str(self.redhead_output) + self.by
            # time.sleep(0.15)
            # if keyboard.is_pressed("a"):
            #     break


if __name__ == "__main__":
    cs = Client()
    cs.output()



    print("ggwp")