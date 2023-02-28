class BitManipulation:
    def __init__(self):
        self.y_hex1 = 0
        self.y_hex2 = 0
        self.x_hex1 = 0
        self.x_hex2 = 0
        self.y_dec1 = 0
        self.y_dec2 = 0
        self.xp = 0
        self.angvalue = 0
        self.yp = 0

    def x_pos(self, x_hex):
        if len(x_hex) <= 2:
            return int(str(x_hex), 16)
        else:
            self.x_hex1 = int(str(x_hex)[2:4], 16)
            self.x_hex2 = int(str(x_hex)[4:6], 16)
            self.xp = self.x_hex1 - self.x_hex2 -1
            return self.xp

    def y_pos(self, y_hex):
        self.y_hex1 = str(y_hex)[0:2]
        self.y_hex2 = str(y_hex)[2:4]
        self.y_dec1 = int(self.y_hex1, 16)
        self.y_dec2 = int(self.y_hex2, 16)
        if self.y_dec1 < self.y_dec2:
            return self.y_dec2/10
        elif self.y_dec2 > self.y_dec1:
            self.yp = self.y_dec2 - self.y_dec1
            return self.yp/10

    def angle_value(self, angle_hex):
        angle_hex = int(str(angle_hex), 16)
        self.angvalue = angle_hex >> 1
        return self.angvalue

    def angle_degree(self, angle_hex):
        angle_hex = int(str(angle_hex), 16)
        self.angvalue = angle_hex >> 1
        return self.angvalue/10

    def tag_data(self, tag_hex):
        if str(tag_hex) == "40":
            return True
        else:
            return False














