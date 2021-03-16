import PyQt5.QtWidgets as qtw
from PyQt5 import QtSvg, QtCore
import socket
import subprocess

from PyQt5.QtCore import pyqtSlot
from handlers import Button_handler
from utils import Utils

IP = '10.42.0.49' #CHANGEABLE
PORT = 11311
WIDTH = 480
HEIGHT = 800

class Button_handler:

    @pyqtSlot()
    def unbreak(self):
        print('unbreak')
        try:
            subprocess.run('./scripts/unbreak.bash')
        except Exception as e:
            print(e)
            raise

    @pyqtSlot()
    def calibrate(self):
        print('calibrate')

    @pyqtSlot()
    def start(self):
        print('start')

    @pyqtSlot()
    def stop(self):
        print('stop')

class Display(qtw.QWidget):
    def __init__(self, ):
        super().__init__()
        self.setWindowTitle('Controller')
        self.button_layout = qtw.QGridLayout()
        self.button_layout.setColumnStretch(0, 4)
        self.button_layout.setColumnStretch(1, 4)

        self.setFixedSize(WIDTH, HEIGHT)
        self.addUI()
        self.setLayout(self.button_layout)


        self.showFullScreen()

### GENERAL UI ADDER
    def addUI(self):
        self.add_button('START', 3, 1, Button_handler.start)
        self.add_button('STOP', 4, 1, Button_handler.stop)
        self.add_button('UNBREAK', 3, 0, Button_handler.unbreak)
        self.add_button('CALIBRATE', 4, 0, Button_handler.calibrate)
        self.add_svg('imgs/process.svg')

    ### PARTICULAR WIDGET ADDERS
    def add_label(self, text, column_place, row_place):
        label = qtw.QLabel("<font color=red size=40>{}!</font>".format(text))

    def add_svg(self, path):
        svg_widget = QtSvg.QSvgWidget(path)
        svg_widget.setFixedSize(100, 100)
        self.button_layout.addWidget(svg_widget, 0, 0, 2, 2, alignment=QtCore.Qt.AlignCenter)

    def add_button(self, name, column_place, row_place, func):
        btn = qtw.QPushButton(name)
        btn.setFixedSize(230, 130)
        btn.clicked.connect(func)

        #just a shadow design
        shadow = qtw.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QtCore.Qt.lightGray)

        btn.setGraphicsEffect(shadow)

        self.button_layout.addWidget(btn, column_place, row_place)

### HELPERS
    # def place_HV_widget(self, obj, placement, container = None):
    #     if container is not None:
    #         container.layout().addWidget(obj, placement)
    #     else:
    #         self.layout().addWidget(obj, placement)
    #
    # def place_grid_widget(self, obj, column_place, row_place, container = None):
    #     if container is not None:
    #         container.layout().addWidget(obj, column_place, row_place)
    #     else:
    #         self.layout().addWidget(obj, column_place, row_place)

def start():
    # global client
    # try:
    #     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     client.connect((IP, int(PORT)))
    # except Exception as e:
    #     print(e)
    subprocess.run('./scripts/start.bash')

    app = qtw.QApplication([])
    mw = Display()
    mw.setFixedSize(HEIGHT, WIDTH)

    with open('style.qss', 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    app.exec_()


if __name__ == '__main__':
    start()
