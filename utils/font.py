import sys
import PyQt5.QtWidgets as qtw

class fontdialogdemo(qtw.QWidget):
    def __init__(self, parent=None):
        super(fontdialogdemo, self).__init__(parent)

        layout = qtw.QVBoxLayout()
        self.btn = qtw.QPushButton("choose font")
        self.btn.clicked.connect(self.getfont)

        layout.addWidget(self.btn)
        self.le = qtw.QLabel("Hello")

        layout.addWidget(self.le)
        self.setLayout(layout)
        self.setWindowTitle("Font Dialog demo")

    def getfont(self):
        font, ok = qtw.QFontDialog.getFont()

        if ok:
            self.le.setFont(font)


def main():
    app = qtw.QApplication(sys.argv)
    ex = fontdialogdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()