import sys


from PyQt5 import uic
from random import randint as ri
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QColor
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.DrawButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            f_r, s_r = ri(1, 100), ri(1, 100)
            yellow_color = QColor(255, 255, 0)
            qp.setBrush(yellow_color)
            qp.drawEllipse(QPointF(150, 150), f_r, s_r)
            qp.drawEllipse(QPointF(150 + f_r * 2, 150), f_r, s_r)
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
