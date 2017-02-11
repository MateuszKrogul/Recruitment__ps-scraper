from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont, QFontMetrics, QRegion
from PyQt5.QtCore import QSize, Qt
import sys

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initLoginScreen()

    def initLoginScreen(self):

        # font
        font = QFont("Arial", 23)

        # background image
        image = QImage("./Graphics/background.gif")
        image = image.scaled(QSize(500,300))

        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

        # labels
        l_username = QLabel("nr indeksu", self)
        l_username.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.Foreground, Qt.white)
        l_username.setPalette(palette)
        l_username.move(120,170)

        l_password = QLabel("hasło", self)
        l_password.setFont(font)
        l_password.setPalette(palette)
        l_password.move(120, 200)

        font = QFont("Arial", 18)
        metrics = QFontMetrics(font)

        # line edits
        le_username = QLineEdit(self)
        le_username.setFont(QFont("Arial", 16))
        le_username.setFixedSize(metrics.width("888888888888"), metrics.height())
        le_username.move(260,l_username.y()+(l_username.height()/2)-(le_username.height()/2)) # center lineEdit
        le_username.setAttribute(Qt.WA_MacShowFocusRect, 0)
        le_username.setFocus()

        le_password = QLineEdit(self)
        le_password.setFont(font)
        le_password.setFixedSize(metrics.width("888888888888"), metrics.height())
        le_password.move(260, l_password.y() + (l_password.height()/2) - (le_password.height()/2)) # center lineEdit
        le_password.setAttribute(Qt.WA_MacShowFocusRect,0)
        le_password.setEchoMode(QLineEdit.Password)

        # button
        submit = QPushButton(self)
        submit.setFont(font)

        submit.setStyleSheet("background-color: white")

        submit.setText("zaloguj")
        submit.setFixedSize(le_password.width(),le_password.height()+7)
        submit.move(260, 240)

        # window settings
        self.setFixedSize(500, 300)
        self.setWindowTitle("Ps scraper")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()

    sys.exit(app.exec_())