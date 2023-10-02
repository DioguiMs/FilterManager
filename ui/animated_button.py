# animated_button.py

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect


class AnimatedButton(QPushButton):
    def __init__(self, parent=None):
        super(AnimatedButton, self).__init__(parent)
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1200)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)

    def enterEvent(self, event):
        self.animation.setStartValue(self.geometry())
        self.setStyleSheet("border: 2px solid red; border-radius: 5px; max-width: 45px; max-height: 22px; background-color: red; color: white;")
        self.animation.setEndValue(QRect(self.x(), self.y(), self.width(), self.height()))
        self.animation.start()

    def leaveEvent(self, event):
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QRect(self.x(), self.y(), self.width(), self.height()))
        self.animation.start()

        self.setStyleSheet("border: none; width: 45px; height: 20px; max-width: 45px; max-height: 20px; background-color: black; color: red;")

class RunAnimatedButton(QPushButton):
    def __init__(self, parent=None):
        super(RunAnimatedButton, self).__init__(parent)
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1200)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)

    def enterEvent(self, event):
        self.animation.setStartValue(self.geometry())
        self.setStyleSheet("background-color: red; color: white;")
        self.animation.setEndValue(QRect(self.x(), self.y(), self.width(), self.height()))
        self.animation.start()

    def leaveEvent(self, event):
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QRect(self.x(), self.y(), self.width(), self.height()))
        self.animation.start()

        self.setStyleSheet("background-color: black; color: red;")