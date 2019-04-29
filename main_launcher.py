#!/usr/bin/python
import qdarkgraystyle
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen
import time
import json

from MainWindow import MainWindow

if __name__ == "__main__":
    settings = open("default/userDefault.json")
    settings_text = ''
    for line in settings:
        settings_text += line
    settings.close()
    settings_dict = json.loads(settings_text)
    app = QApplication([])
    if settings_dict['dark-mode'] == 'true':
        app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    if settings_dict['show-splash'] == 'true':
        for i in range(5):
            splash = QSplashScreen()
            splash.setPixmap(QPixmap('./Icons/loading_' + str(i) + '.png'))
            splash.show()
            time.sleep(0.3)
            splash.hide()
    window = MainWindow()
    window.show()
    app.exec_()