import PyQt5.QtWidgets as qtw
from PyQt5 import QtSvg, QtCore
import socket


from handlers import Button_handlers
from utils import Utils

IP = '127.0.0.1' #CHANGEABLE
PORT = 8888
WIDTH = 480
HEIGHT = 320

class Display(qtw.QWidget):
    def __init__(self, client):
        super().__init__()
        self.setWindowTitle('Controller')
        self.button_layout = qtw.QGridLayout()
        self.setFixedSize(HEIGHT, WIDTH)
        self.addUI()
        self.setLayout(self.button_layout)

        self.client = client

        self.show()

### GENERAL UI ADDER
    def addUI(self):
        self.add_svg('imgs/process.svg')
        self.add_button('calibrate', 1, 0, Button_handlers.calibrate)
        self.add_button('unbreak', 1, 1, Button_handlers.unbreak)
        self.add_button('stop', 2, 0, Button_handlers.stop)
        self.add_button('start', 2, 1, Button_handlers.start)

    ### PARTICULAR WIDGET ADDERS
    def add_label(self, text, column_place, row_place):
        label = qtw.QLabel("<font color=red size=40>{}!</font>".format(text))

    def add_svg(self, path):
        svg_widget = QtSvg.QSvgWidget(path)
        svg_widget.setFixedSize(100, 100)
        self.button_layout.addWidget(svg_widget, 0, 0, 1, 2, alignment=QtCore.Qt.AlignCenter)

    def add_button(self, name, column_place, row_place, func):
        btn = qtw.QPushButton(name)
        btn.setFixedSize(100, 50)
        btn.clicked.connect(func)
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
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, int(PORT)))
    except Exception as e:
        print(e)

    app = qtw.QApplication([])
    mw = Display(client)
    mw.setFixedSize(HEIGHT, WIDTH)

    with open('style.qss', 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    app.exec_()


if __name__ == '__main__':
    start()
