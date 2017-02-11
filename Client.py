from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import sys

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(500,300)


        image = QImage("./Graphics/background.gif")
        image = image.scaled(QSize(500,300))

        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

        self.setWindowTitle("Ps scraper")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()

    sys.exit(app.exec_())