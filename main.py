from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QMainWindow
from PyQt5.QtCore import QSize
from threading import Thread
from subprocess import call
from platform import system
from time import sleep
import lang_theme


class App(QWidget):
    def __init__(self, language: str = "en"):
        super().__init__()
        self.language = lang_theme.languages(language)
        self.language = self.language.getWords()
        self.title = f'{self.language["title"]}'
        self.left = 800
        self.top = 300
        self.width = 350
        self.height = 275
        self.status = False
        self.arayuz()

    def arayuz(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(QSize(self.width, self.height))
        self.setStyleSheet(lang_theme.theme("dark").getTheme())

        self.lngBtn = QPushButton(self)
        self.lngBtn.setText(self.language["lngBtn"])
        self.lngBtn.setObjectName("lngButton")
        self.lngBtn.move(215, 240)
        self.lngBtn.resize(125, 25)

        self.themeBtn = QPushButton(self)
        self.themeBtn.setText(self.language["themeBtnOn"])
        self.themeBtn.setObjectName("themeButton")
        self.themeBtn.move(295, 5)
        self.themeBtn.resize(50, 25)

        self.sdLbl = QLabel(self)
        self.sdLbl.setText("SD")
        self.sdLbl.setObjectName("sd")
        self.sdLbl.move(155, 15)

        self.timeLE = QLineEdit(
            self, placeholderText=self.language["enterTime"])
        self.timeLE.move(100, 85)
        self.timeLE.resize(170, 30)

        self.startBtn = QPushButton(self)
        self.startBtn.setText(self.language["startBtn"])
        self.startBtn.setObjectName("startButton")
        self.startBtn.move(125, 135)
        self.startBtn.resize(125, 25)

        self.cancelBtn = QPushButton(self)
        self.cancelBtn.setText(self.language["cancelBtn"])
        self.cancelBtn.move(125, 170)
        self.cancelBtn.resize(125, 25)

        self.statusLbl = QLabel(self)
        self.statusLbl.setText(self.language["statusLbl"])
        self.statusLbl.move(15, 240)
        self.statusLbl.resize(100, 20)

        self.status_F_Lbl = QLabel(self)
        self.status_F_Lbl.setObjectName("status")
        self.status_F_Lbl.setText("False")
        self.status_F_Lbl.move(65, 240)
        self.status_F_Lbl.resize(100, 20)

        self.timerLbl = QLabel(self)
        self.timerLbl.setText(self.language["timerLbl"])
        self.timerLbl.move(15, 210)
        self.timerLbl.resize(100, 20)

        self.timer_F_Lbl = QLabel(self)
        self.timer_F_Lbl.setObjectName("timer")
        self.timer_F_Lbl.setStyleSheet("color: #f00;")
        self.timer_F_Lbl.setText("False")
        self.timer_F_Lbl.move(60, 210)
        self.timer_F_Lbl.resize(100, 20)

        self.lngBtn.clicked.connect(self.changeLng)
        self.startBtn.clicked.connect(self.start)
        self.cancelBtn.clicked.connect(self.cancel)
        self.themeBtn.clicked.connect(self.changeTheme)

    def changeTheme(self):
        if self.themeBtn.text() == self.language["themeBtnOff"]:
            self.setStyleSheet(lang_theme.theme("dark").getTheme())
            self.themeBtn.setText(self.language["themeBtnOn"])
        elif self.themeBtn.text() == self.language["themeBtnOn"]:
            self.setStyleSheet(lang_theme.theme("light").getTheme())
            self.themeBtn.setText(self.language["themeBtnOff"])

    def changeLng(self):
        if self.language == lang_theme.languages("en").getWords():
            self.language = lang_theme.languages("tr").getWords()
            self.setWindowTitle(self.language["title"])
            self.lngBtn.setText(self.language["lngBtn"])
            self.timeLE.setPlaceholderText(self.language["enterTime"])
            self.startBtn.setText(self.language["startBtn"])
            self.cancelBtn.setText(self.language["cancelBtn"])
            self.statusLbl.setText(self.language["statusLbl"])
            self.timerLbl.setText(self.language["timerLbl"])
            self.themeBtn.setText(self.language["themeBtnOn"])
        elif self.language == lang_theme.languages("tr").getWords():
            self.language = lang_theme.languages("de").getWords()
            self.setWindowTitle(self.language["title"])
            self.lngBtn.setText(self.language["lngBtn"])
            self.timeLE.setPlaceholderText(self.language["enterTime"])
            self.startBtn.setText(self.language["startBtn"])
            self.cancelBtn.setText(self.language["cancelBtn"])
            self.statusLbl.setText(self.language["statusLbl"])
            self.timerLbl.setText(self.language["timerLbl"])
            self.themeBtn.setText(self.language["themeBtnOn"])
        elif self.language == lang_theme.languages("de").getWords():
            self.language = lang_theme.languages("fr").getWords()
            self.setWindowTitle(self.language["title"])
            self.lngBtn.setText(self.language["lngBtn"])
            self.timeLE.setPlaceholderText(self.language["enterTime"])
            self.startBtn.setText(self.language["startBtn"])
            self.cancelBtn.setText(self.language["cancelBtn"])
            self.statusLbl.setText(self.language["statusLbl"])
            self.timerLbl.setText(self.language["timerLbl"])
            self.themeBtn.setText(self.language["themeBtnOn"])
        elif self.language == lang_theme.languages("fr").getWords():
            self.language = lang_theme.languages("en").getWords()
            self.setWindowTitle(self.language["title"])
            self.lngBtn.setText(self.language["lngBtn"])
            self.timeLE.setPlaceholderText(self.language["enterTime"])
            self.startBtn.setText(self.language["startBtn"])
            self.cancelBtn.setText(self.language["cancelBtn"])
            self.statusLbl.setText(self.language["statusLbl"])
            self.timerLbl.setText(self.language["timerLbl"])
            self.themeBtn.setText(self.language["themeBtnOn"])

    def start(self):
        if self.timeLE.text() == "":
            QMessageBox.warning(
                self, self.language["warning"], self.language["warningText"])
        else:
            self.status = True
            self.status_F_Lbl.setStyleSheet("color: #0f0;")
            self.status_F_Lbl.setText("True")
            self.timer_F_Lbl.setStyleSheet("color: #ffff00;")
            if system() == "Windows":
                self.time = int(self.timeLE.text()) * 60
                Thread(target=self.timer).start()
                call(["shutdown", "-s", "-t", str(self.time)])
            elif system() == "Linux":
                self.time = int(self.timeLE.text())
                Thread(target=self.timer).start()
                call(["shutdown", "-h", "+" + str(self.time)])
            elif system() == "Darwin":
                self.time = int(self.timeLE.text()) * 60
                Thread(target=self.timer).start()
                call(["sudo shutdown", "-h", "+" + str(self.time)])

    def cancel(self):
        self.status = False
        self.status_F_Lbl.setText("False(cancelled)")
        self.timer_F_Lbl.setText("False")
        self.status_F_Lbl.setStyleSheet("color: #f00;")
        self.timer_F_Lbl.setStyleSheet("color: #f00;")
        if system() == "Windows":
            call(["shutdown", "-a"])
        elif system() == "Linux":
            call(["shutdown", "-c"])
        elif system() == "Darwin":
            call(["sudo shutdown", "-c"])

    def timer(self):
        while self.time > 0:
            if self.status == False:
                break
            self.saat = self.time // 3600
            self.dakika = (self.time % 3600) // 60
            self.saniye = (self.time % 3600) % 60
            self.zaman = "{:02}:{:02}:{:02}".format(
                self.saat, self.dakika, self.saniye)
            self.updateGui()
            self.time -= 1
            sleep(1)

    def updateGui(self):
        self.timer_F_Lbl.setText(str(self.zaman))


if __name__ == "__main__":
    from sys import argv, exit
    app = QApplication(argv)
    ex = App()
    ex.show()
    exit(app.exec_())
