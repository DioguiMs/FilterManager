# main.py

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from ui.main_window import MainWindow
from PyQt5.QtCore import QResource, QFile, QTextStream
import resources

sys.path.append(".")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    font = QFont(":/styles/assets/font/Georama-Light.ttf")
    print(font)
        
    css_file = QFile(":/styles/assets/styles.css")
        
    if css_file.open(QFile.ReadOnly | QFile.Text): # type: ignore
        stream = QTextStream(css_file)
        app.setStyleSheet(stream.readAll())
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
