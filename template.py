# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.footer = QtWidgets.QLabel(self.centralwidget)
        self.footer.setGeometry(QtCore.QRect(0, 130, 501, 16))
        self.footer.setAlignment(QtCore.Qt.AlignCenter)
        self.footer.setObjectName("footer")
        self.startBut = QtWidgets.QPushButton(self.centralwidget)
        self.startBut.setGeometry(QtCore.QRect(390, 30, 101, 30))
        self.startBut.setObjectName("startBut")
        self.lineHotKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineHotKey.setGeometry(QtCore.QRect(10, 30, 31, 30))
        self.lineHotKey.setMaxLength(1)
        self.lineHotKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lineHotKey.setObjectName("lineHotKey")
        self.info_1 = QtWidgets.QLabel(self.centralwidget)
        self.info_1.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.info_1.setObjectName("info_1")
        self.lineMainKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineMainKey.setGeometry(QtCore.QRect(310, 30, 31, 30))
        self.lineMainKey.setMaxLength(1)
        self.lineMainKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lineMainKey.setObjectName("lineMainKey")
        self.info_2 = QtWidgets.QLabel(self.centralwidget)
        self.info_2.setGeometry(QtCore.QRect(280, 10, 101, 16))
        self.info_2.setObjectName("info_2")
        self.lineHotKey_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineHotKey_2.setGeometry(QtCore.QRect(50, 30, 31, 30))
        self.lineHotKey_2.setMaxLength(1)
        self.lineHotKey_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineHotKey_2.setObjectName("lineHotKey_2")
        self.lineHotKey_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineHotKey_3.setGeometry(QtCore.QRect(90, 30, 31, 30))
        self.lineHotKey_3.setMaxLength(1)
        self.lineHotKey_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineHotKey_3.setObjectName("lineHotKey_3")
        self.lineHotKey_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineHotKey_4.setGeometry(QtCore.QRect(130, 30, 31, 30))
        self.lineHotKey_4.setMaxLength(1)
        self.lineHotKey_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineHotKey_4.setObjectName("lineHotKey_4")
        self.lineHotKey_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineHotKey_5.setGeometry(QtCore.QRect(170, 30, 31, 30))
        self.lineHotKey_5.setMaxLength(1)
        self.lineHotKey_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineHotKey_5.setObjectName("lineHotKey_5")
        self.lineHotKey_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineHotKey_6.setGeometry(QtCore.QRect(210, 30, 31, 30))
        self.lineHotKey_6.setMaxLength(1)
        self.lineHotKey_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineHotKey_6.setObjectName("lineHotKey_6")
        self.info_3 = QtWidgets.QLabel(self.centralwidget)
        self.info_3.setGeometry(QtCore.QRect(10, 60, 231, 31))
        self.info_3.setScaledContents(False)
        self.info_3.setWordWrap(True)
        self.info_3.setObjectName("info_3")
        self.info_4 = QtWidgets.QLabel(self.centralwidget)
        self.info_4.setGeometry(QtCore.QRect(390, 60, 101, 16))
        self.info_4.setObjectName("info_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.footer.setText(_translate("MainWindow", "Разработал Daiki Hanma, daikihanma@outlook.com"))
        self.startBut.setText(_translate("MainWindow", "Старт"))
        self.info_1.setText(_translate("MainWindow", "То что будет нажато по горячей клавише"))
        self.info_2.setText(_translate("MainWindow", "Горячая клавиша"))
        self.info_3.setText(_translate("MainWindow", "Если клавиша не нужна, оставьте поле пустым"))
        self.info_4.setText(_translate("MainWindow", "Для остановки F11"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
