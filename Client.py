from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import QSize, Qt
import sys

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initLoginScreen()

    def initLoginScreen(self):

        # background image
        image = QImage("./Graphics/background.gif")
        image = image.scaled(QSize(500,300))

        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

        l_username = QLabel("nr indeksu", self)
        l_username.setFont(QFont("Arial",23))

        palette = QPalette()
        palette.setColor(QPalette.Foreground, Qt.white)
        l_username.setPalette(palette)
        l_username.move(120,170)

        l_password = QLabel("hasło", self)
        l_password.setFont(QFont("Arial", 23))
        l_password.setPalette(palette)
        l_password.move(120, 200)

        font = QFont()
        font.setFamily("")

        self.setFixedSize(500, 300)
        self.setWindowTitle("Ps scraper")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()

    sys.exit(app.exec_())