# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIBrazo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelR = QtWidgets.QLabel(self.centralwidget)
        self.labelR.setGeometry(QtCore.QRect(290, 250, 191, 111))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.labelR.setFont(font)
        self.labelR.setStyleSheet("")
        self.labelR.setTextFormat(QtCore.Qt.AutoText)
        self.labelR.setAlignment(QtCore.Qt.AlignCenter)
        self.labelR.setObjectName("labelR")
        self.labelL = QtWidgets.QLabel(self.centralwidget)
        self.labelL.setGeometry(QtCore.QRect(0, 250, 201, 111))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelL.setFont(font)
        self.labelL.setStyleSheet("")
        self.labelL.setAlignment(QtCore.Qt.AlignCenter)
        self.labelL.setObjectName("labelL")
        self.labelS = QtWidgets.QLabel(self.centralwidget)
        self.labelS.setGeometry(QtCore.QRect(210, 250, 61, 111))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.labelS.setFont(font)
        self.labelS.setStyleSheet("")
        self.labelS.setAlignment(QtCore.Qt.AlignCenter)
        self.labelS.setObjectName("labelS")
        self.commitOperation = QtWidgets.QPushButton(self.centralwidget)
        self.commitOperation.setGeometry(QtCore.QRect(327, 470, 141, 27))
        self.commitOperation.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.commitOperation.setObjectName("commitOperation")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(230, 470, 88, 27))
        self.reset.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.reset.setObjectName("reset")
        self.b0m1 = QtWidgets.QPushButton(self.centralwidget)
        self.b0m1.setGeometry(QtCore.QRect(0, 0, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.b0m1.setFont(font)
        self.b0m1.setObjectName("b0m1")
        self.b00 = QtWidgets.QPushButton(self.centralwidget)
        self.b00.setGeometry(QtCore.QRect(160, 0, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.b00.setFont(font)
        self.b00.setObjectName("b00")
        self.b01 = QtWidgets.QPushButton(self.centralwidget)
        self.b01.setGeometry(QtCore.QRect(320, 0, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.b01.setFont(font)
        self.b01.setObjectName("b01")
        self.b1m1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1m1.setGeometry(QtCore.QRect(0, 90, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.b1m1.setFont(font)
        self.b1m1.setObjectName("b1m1")
        self.b10 = QtWidgets.QPushButton(self.centralwidget)
        self.b10.setGeometry(QtCore.QRect(160, 90, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.b10.setFont(font)
        self.b10.setObjectName("b10")
        self.b11 = QtWidgets.QPushButton(self.centralwidget)
        self.b11.setGeometry(QtCore.QRect(320, 90, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.b11.setFont(font)
        self.b11.setObjectName("b11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelR.setText(_translate("MainWindow", "(x2,y2)"))
        self.labelL.setText(_translate("MainWindow", "(x1,y1)"))
        self.labelS.setText(_translate("MainWindow", ">"))
        self.commitOperation.setText(_translate("MainWindow", "Commit Operation"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.b0m1.setText(_translate("MainWindow", "(0,-1)"))
        self.b00.setText(_translate("MainWindow", "(0,0)"))
        self.b01.setText(_translate("MainWindow", "(0,1)"))
        self.b1m1.setText(_translate("MainWindow", "(1,-1)"))
        self.b10.setText(_translate("MainWindow", "(1,0)"))
        self.b11.setText(_translate("MainWindow", "(1,1)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

