import PyQt5.QtWidgets as qtw
import socket

IP = '127.0.0.1' #CHANGEABLE
PORT = 8888

class Display(qtw.QWidget):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.setWindowTitle('Controller')
        self.setLayout(qtw.QGridLayout())


        self.ubreak_button("Unbreak", 0, 0)
        self.calibrate_button("Calibrate", 1, 0)
        self.random1_button("Random1", 0, 1)
        self.random2_button("Random2", 1, 1)

        self.show()


    # Unbreak button
    def ubreak_button(self, name, column_place, row_place, container: qtw.QWidget = None):
        btn = qtw.QPushButton(name, clicked=self.unbreak)
        self.add_button(btn, column_place, row_place, container)

    def unbreak(self):
        print('unbreak')
        try:
            self.client.send("unbreak".encode())
        except Exception as e:
            print(e)
            raise

    # Calibrate button
    def calibrate_button(self, name, column_place, row_place, container: qtw.QWidget = None):
        btn = qtw.QPushButton(name, clicked=self.calibrate)
        self.add_button(btn, column_place, row_place, container)

    def calibrate(self):
        print('calibrate')

    # Random1 button
    def random1_button(self, name, column_place, row_place, container: qtw.QWidget = None):
        btn = qtw.QPushButton(name, clicked=self.random1)
        self.add_button(btn, column_place, row_place, container)

    def random1(self):
        print('random1')

    # Random2 button
    def random2_button(self, name, column_place, row_place, container: qtw.QWidget = None):
        btn = qtw.QPushButton(name, clicked=self.random2)
        self.add_button(btn, column_place, row_place, container)

    def random2(self):
        print('random2')

    # Utils
    def add_button(self, btn, column_place, row_place, container: qtw.QWidget = None):
        if container is not None:
            container.layout().addWidget(btn, column_place, row_place)
        else:
            self.layout().addWidget(btn, column_place, row_place)



def start():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, int(PORT)))

    app = qtw.QApplication([])
    mw = Display(client)

    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    app.exec_()


if __name__ == '__main__':
    start()
