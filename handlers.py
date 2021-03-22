from PyQt5.QtCore import pyqtSlot
import subprocess
import PyQt5.QtWidgets as qtw

from pygt import MainWindow

class Button_handler:

    @pyqtSlot()
    def unbreak(self):
        print('unbreak')
        # try:
        #     subprocess.call('./scripts/unbreak.bash')
        # except Exception as e:
        #     print(e)
        #     raise

    @pyqtSlot()
    def calibrate(self, window: MainWindow):
        print('calibrate')

    @pyqtSlot()
    def start(self):
        print('start')

    @pyqtSlot()
    def stop(self):
        print('stop')

