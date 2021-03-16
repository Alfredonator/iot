from PyQt5.QtCore import pyqtSlot

class Button_handler:

    @pyqtSlot()
    def unbreak(self):
        print('unbreak')
        try:
            self.client.send("unbreak".encode())
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

