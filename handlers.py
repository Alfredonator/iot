from PyQt5.QtCore import pyqtSlot
import subprocess


class Button_handler:

    @pyqtSlot()
    def unbreak(self):
        print('unbreak')
        try:
            subprocess.call('../scripts/unbreak.bash')
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

