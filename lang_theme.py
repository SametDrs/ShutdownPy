class languages:
    def __init__(self, lang: str):
        self.lang = lang

    def tr(self):
        trW = {
            "title": "Kapatma Zamanlayıcısı",
            "startBtn": "Başlat",
            "cancelBtn": "İptal Et",
            "timerLbl": "Sayaç: ",
            "statusLbl": "Durum: ",
            "enterTime": "Süreyi dk olarak giriniz",
            "lngBtn": "Dili değiştir",
            "warning": "Uyarı",
            "warningText": "Bir sayı girmelisiniz",
            "themeBtnOn": "Açık",
            "themeBtnOff": "Kapalı"
        }
        return trW

    def en(self):
        enW = {
            "title": "Shutdown Timer",
            "startBtn": "Start",
            "cancelBtn": "Cancel",
            "timerLbl": "Timer: ",
            "statusLbl": "Status: ",
            "enterTime": "Enter time in minutes",
            "lngBtn": "Change language",
            "warning": "Warning",
            "warningText": "You must enter a number",
            "themeBtnOn": "Light",
            "themeBtnOff": "Dark"
        }
        return enW

    def de(self):
        deW = {
            "title": "Shutdown Timer",
            "startBtn": "Anfang",
            "cancelBtn": "Abbrechen",
            "timerLbl": "Timer: ",
            "statusLbl": "Status: ",
            "enterTime": "Geben Sie die Zeit in Minuten ein",
            "lngBtn": "Sprache ändern",
            "warning": "Warnung",
            "warningText": "Sie müssen eine Zahl eingeben",
            "themeBtnOn": "Licht",
            "themeBtnOff": "Dunkler"
        }
        return deW

    def fr(self):
        frW = {
            "title": "Minuterie de Fermeture",
            "startBtn": "Début",
            "cancelBtn": "Annuler",
            "timerLbl": "Minuteur: ",
            "statusLbl": "Statut: ",
            "enterTime": "Entrez le temps en minutes",
            "lngBtn": "Changer de langue",
            "warning": "Avertissement",
            "warningText": "Vous devez entrer un nombre",
            "themeBtnOn": "lumière",
            "themeBtnOff": "Sombre"
        }
        return frW

    def getWords(self):
        if self.lang == "tr":
            return self.tr()
        elif self.lang == "en":
            return self.en()
        elif self.lang == "de":
            return self.de()
        elif self.lang == "fr":
            return self.fr()
        else:
            return self.en()


class theme:
    def __init__(self, theme: str):
        self.theme = theme

    def light(self):
        light = """
            QWidget {
                color: #000;
                background-color: #fff;
            }
            QPushButton {
                background-color: #eee;
                font-size: 12px;
                font-weight: bold;
                border-radius: 5px;
                border: 1px solid #000;
            }
            QPushButton:hover {
                background-color: #ddd;
            }
            QPushButton:pressed {
                background-color: #ccc;
            }
            QLineEdit {
                background-color: #eee;
                font-size: 12px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
                border: 1px solid #000;
            }
            QLabel {
                font-size: 12px;
                font-weight: bold;
            }
            QLabel#status {
                color: #f00;
            }
            QLabel#sd {
                font-size: 42px;
            }
            QLabel#timeLabel {
                font-size: 14px;
            }
            QLabel#sd {
                font-size: 42px;
            }
            QMessageBox {
                background-color: #fff;
            }
        """
        return light

    def dark(self):
        dark = """
            QWidget {
                color: #fff;
                background-color: #111;
            }
            QPushButton {
                background-color: #1f1f1f;
                font-size: 12px;
                font-weight: bold;
                border-radius: 5px;
                border: 1px solid #000;
            }
            QPushButton:hover {
                background-color: #2f2f2f;
            }
            QPushButton:pressed {
                background-color: #3f3f3f;
            }
            QLineEdit {
                background-color: #1f1f1f;
                font-size: 12px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
                border: 1px solid #000;
            }
            QLabel {
                font-size: 12px;
                font-weight: bold;
            }
            QLabel#status {
                color: #f00;
            }
            QLabel#sd {
                font-size: 42px;
            }
            QLabel#timeLabel {
                font-size: 14px;
            }
            QLabel#sd {
                font-size: 42px;
            }
            QMessageBox {
                background-color: #111;
            }
            """
        return dark

    def getTheme(self):
        if self.theme == "light":
            return self.light()
        elif self.theme == "dark":
            return self.dark()
        else:
            return self.dark()
