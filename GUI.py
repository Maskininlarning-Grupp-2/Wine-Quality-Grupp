import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Wine Quality Prediction')
        self.setFixedSize(400, 600)

app = QApplication(sys.argv)

window = Window()

window.show()