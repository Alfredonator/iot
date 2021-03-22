import PyQt5.QtWidgets as qtw
from PyQt5 import QtSvg, QtCore
import subprocess
from PyQt5.QtGui import QFont
import os
from env import set_env_var

set_env_var()
ip = os.getenv('IP')
port = int(os.getenv('PORT'))
height = int(os.getenv('HEIGHT'))
width = int(os.getenv('WIDTH'))
is_raspberry = bool(os.getenv('RASP'))

class Calibration_view(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.joint_counter = 1

        layout = qtw.QGridLayout()

        svg_icon = add_svg('imgs/robotics.svg')

        self.label = qtw.QLabel("Joint number: {}".format(self.joint_counter))

        self.btn_next = add_button('CALIBRATE NEXT JOINT', self.next_joint, 260)
        self.btn_next.setStyleSheet('background-color: gold')
        shade_calib_btn = add_shadow()
        self.btn_next.setGraphicsEffect(shade_calib_btn)

        layout.addWidget(svg_icon, 0, 0, 1, 1, alignment=QtCore.Qt.AlignRight)
        layout.addWidget(self.label, 0, 1, 1, 2, alignment=QtCore.Qt.AlignLeft)
        layout.addWidget(self.btn_next, 0, 2, alignment=QtCore.Qt.AlignCenter)

        btn_right = add_button('>', self.arrow_right, 150, 100)
        btn_left = add_button('<', self.arrow_left, 150, 100)
        btn_up = add_button('^', self.arrow_up, 150, 100)
        btn_down = add_button('.', self.arrow_down, 150, 100)
        btn_break = add_button('UNBREAK', unbreak, 190, 100)
        btn_break.setStyleSheet('background-color: chocolate')
        shade_unbreak_btn = add_shadow()
        btn_break.setGraphicsEffect(shade_unbreak_btn)

        layout.addWidget(btn_left, 2, 0, alignment=QtCore.Qt.AlignRight)
        layout.addWidget(btn_break, 2, 1, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(btn_right, 2, 2, alignment=QtCore.Qt.AlignLeft)
        layout.addWidget(btn_up, 1, 1, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(btn_down, 3, 1, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(layout)

    def arrow_left(self):
        print('<')

    def arrow_right(self):
        print('<')

    def arrow_down(self):
        print('down')

    def arrow_up(self):
        print('^')

    def next_joint(self):
        self.joint_counter += 1
        self.label.setText("Joint number: {}".format(self.joint_counter))
        print('next joint: {}'.format(self.joint_counter))
        if self.joint_counter == 6:
            self.btn_next.setText('FINISH')
        if self.joint_counter > 6:
            self.joint_counter = 0
            print(self.joint_counter)
            self.btn_next.setText('CALIBRATE NEXT JOINT')
            self.close()


class Display(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Controller')
        self.button_layout = qtw.QGridLayout()
        self.button_layout.setColumnStretch(0, 2)
        self.button_layout.setColumnStretch(1, 2)
        self.calibration_gui = Calibration_view()

        self.addUI()
        self.setLayout(self.button_layout)

        if is_raspberry:
            self.showFullScreen()
        else:
            self.setFixedSize(width, height)
            self.show()


    ### GENERAL UI ADDER
    def addUI(self):
        label = qtw.QLabel("Status: {}".format('robot status'))
        self.button_layout.addWidget(label, 0, 0, 1, 2, alignment=QtCore.Qt.AlignRight)

        svg_icon = add_svg('imgs/process.svg')
        self.button_layout.addWidget(svg_icon, 0, 0, 1, 2, alignment=QtCore.Qt.AlignCenter)

        btn1 = add_button('START', self.start)
        btn2 = add_button('STOP', self.stop)
        btn3 = add_button('UNBREAK', unbreak)
        btn4 = add_button('CALIBRATE', self.show_calibration)

        self.button_layout.addWidget(btn1, 1, 1)
        self.button_layout.addWidget(btn2, 1, 0)
        self.button_layout.addWidget(btn3, 2, 0)
        self.button_layout.addWidget(btn4, 2, 1)

    ### PARTICULAR WIDGET ADDERS
    def show_calibration(self):
        if is_raspberry:
            self.calibration_gui.showFullScreen()
        else:
            self.calibration_gui.setFixedSize(width, height)
            self.calibration_gui.show()

    def start(self):
        print('start')

    def stop(self):
        print('stop')

###COMMONS
def add_svg(path):
    svg_widget = QtSvg.QSvgWidget(path)
    svg_widget.setFixedSize(100, 100)
    return svg_widget

def unbreak(self):
    if not is_raspberry:
        print('unbreak')
    else:
        try:
            subprocess.call('./scripts/unbreak.bash')
        except Exception as e:
            print(e)
            raise

def add_shadow():
    shadow = qtw.QGraphicsDropShadowEffect()
    shadow.setBlurRadius(20)
    shadow.setColor(QtCore.Qt.lightGray)
    return shadow

def add_button(name, func, wid=230, hei=130):
        btn = qtw.QPushButton(name)
        btn.setFixedSize(wid, hei)
        btn.clicked.connect(func)
        shade = add_shadow()
        btn.setGraphicsEffect(shade)
        return btn

def start():

    app = qtw.QApplication([])
    app.setFont(QFont('Microsoft YaHei Light', 13))
    mw = Display()
    mw.setFixedSize(width, height)
    if is_raspberry:
        subprocess.run('./scripts/start.bash')
        mw.showFullScreen()
    else:
        mw.show()

    with open('style.qss', 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    app.exec_()


if __name__ == '__main__':
    start()
