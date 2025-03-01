import sys
from random import randint

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor


SIZE = [800, 600]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.btn.clicked.connect(self.draw)


    def draw(self):
        self.figure = 'circle'
        self.color = (255, 255, 0)
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(*self.color))
        qp.setBrush(QColor(*self.color))
        self.n = randint(10, 20)
        for i in range(self.n):
            self.x, self.y = randint(50, SIZE[0] - 50), randint(50, SIZE[1] - 50)
            self.size = randint(10, 50)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
        qp.end()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())