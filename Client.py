from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont, QFontMetrics, QRegion
from PyQt5.QtCore import QSize, Qt, QPropertyAnimation, QRect
import sys, time
import Session

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initLoginScreen()
        self.session = None
        self.courses = []
        self.l_no_courses = None

    def initLoginScreen(self):

        # font
        font = QFont("Arial", 23)

        self.set_background("./Graphics/background.gif")

        # labels
        self.l_username = QLabel("nr indeksu", self)
        self.l_username.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.Foreground, Qt.white)
        self.l_username.setPalette(palette)
        self.l_username.move(120, 170)

        l_password = QLabel("hasło", self)
        l_password.setFont(font)
        l_password.setPalette(palette)
        l_password.move(120, 200)

        palette.setColor(QPalette.Foreground, Qt.red)
        self.message = QLabel("Niepoprawny login lub hasło", self)
        self.message.move(200, 280)
        self.message.setPalette(palette)
        self.message.hide()

        font = QFont("Arial", 18)
        metrics = QFontMetrics(font)

        # line edits
        self.le_username = QLineEdit(self)
        self.le_username.setFont(QFont("Arial", 16))
        self.le_username.setFixedSize(metrics.width("888888888888"), metrics.height())
        self.le_username.move(260, self.l_username.y() + (self.l_username.height() / 2) - (self.le_username.height() / 2)) # center lineEdit
        self.le_username.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.le_username.setFocus()
        self.le_username.textChanged.connect(lambda: (self.message.hide(),
                                                      self.le_username.disconnect()))

        self.le_password = QLineEdit(self)
        self.le_password.setFont(font)
        self.le_password.setFixedSize(metrics.width("888888888888"), metrics.height())
        self.le_password.move(260, l_password.y() + (l_password.height() / 2) - (self.le_password.height() / 2)) # center lineEdit
        self.le_password.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.le_password.setEchoMode(QLineEdit.Password)
        self.le_password.textChanged.connect(lambda : (self.message.hide(),
                                                       self.le_password.disconnect()))

        # button
        submit = QPushButton(self)
        submit.setFont(QFont("Arial", 16))
        submit.setStyleSheet("background-color: solid")
        submit.setText("zaloguj")
        submit.setFixedSize(self.le_password.width(), submit.height() + 3)
        submit.move(260, 240)
        submit.clicked.connect(self.submit_on_clicked)

        # window settings
        self.setFixedSize(500, 300)
        self.setWindowTitle("Ps scraper")
        self.show()

    def initMenuScreen(self):
        self.close()

    def submit_on_clicked(self):
        not_for_docs = None
        '''
        if self.session == None:
            self.session = Session.Session()
        self.session.login(self.le_username.text(), self.le_password.text())

        if not self.session.login(self.le_username.text(), self.le_password.text()): #if wrong pass or username
            self.message.show()
            self.le_username.textChanged.connect(lambda: (self.message.hide(),
                                                          self.le_username.disconnect()))
            self.le_password.textChanged.connect(lambda: (self.message.hide(),
                                                          self.le_password.disconnect()))
            return
        '''

        self.set_background("./Graphics/background.png")
        for i in self.children():
            i.deleteLater()
        '''
        x = 500
        y = 600
        self.setMaximumSize(x,y)
        self.resize(x,y)
        self.setFixedSize(x,y)
        self.move(self.x(), self.y()-200)
        '''

        #terms = self.session.get_terms()
        terms = ["sem1","sem2","sem3","sem4","sem5","sem6"]

        temp_button = QPushButton(self)
        temp_button.setFont(QFont("Arial", 16))
        temp_button.setStyleSheet("background-color: solid")

        x = 5
        n = len(terms)
        gap = 0
        y = (self.height() / 2) - ((n * temp_button.height() + (n - 1) * gap)/2)
        print("{}\n{}\n{}\n{}\n".format(len(terms),self.height(),temp_button.height(), gap))
        print(y)
        del(temp_button)

        self.le_term = []

        for term in terms:
            term_button = QPushButton(self)
            term_button.setFont(QFont("Arial", 16))
            term_button.setStyleSheet("background-color: solid")

            #term_button.setText(terms[term][0])
            term_button.setText(term)
            a = 2
            term_button.move(x, y)
            term_button.show()
            term_button.clicked.connect(lambda:
                                        self.term_button_on_clicked(term_button))
            y += term_button.height() + gap
            self.le_term.extend([term_button])

        '''
        x= self.children()[0].width()+10
        self.setMaximumSize(x, y )
        self.resize(x,y)
        self.setFixedSize(x,y)
        '''
    def term_button_on_clicked(self, button):
        #get courses
        self.courses = ["course1","course2","course3","course4"]
        if len(self.courses) == 0 and self.l_no_courses is not None:
            self.l_no_courses.show()

        if len(self.courses) == 0 and self.l_no_courses is None:
            self.l_no_courses = QLabel("Brak kursów", self)
            self.l_no_courses.setFont(QFont("Arial",18))
            palette = QPalette()
            palette.setColor(QPalette.Foreground, Qt.white)
            self.l_no_courses.setPalette(palette)
            self.l_no_courses.move(button.x()+button.width()+30,50)
            self.l_no_courses.show()


        if len(self.courses) > 0 and self.l_no_courses is not None:
            self.l_no_courses.hide()
        for course in self.courses:
            #TODO create label for course and grade, get grade
            pass




    def set_background(self, path):
        # background image
        image = QImage(path)
        #image = image.scaled(QSize(500, 300))

        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()

    sys.exit(app.exec_())