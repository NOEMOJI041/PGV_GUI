from bitmanipulation import BitManipulation
from client import Client
from pgvgui import Ui_MainWindow
# from PyQt5 import QtWidgets
import sys

cl = Client()
dm = BitManipulation()


td = str(cl)[2:4]
x_data = str(cl)[4:12]
y_data = str(cl)[12:16]
angle_data = str(cl)[16:20]

print(dm.tag_data(td))
print(dm.y_pos(y_data))
print(dm.angle_value(angle_data))
print(dm.angle_degree(angle_data))


# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())


