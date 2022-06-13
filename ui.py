# The code below is done by a PyQt5 Designer and just a little bit manipulated


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 811)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(54)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #771EA1")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("background-color: #771EA1")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-80, -60, 1001, 171))
        self.frame.setStyleSheet("background-color: #3E6FE7")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 70, 771, 91))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #3E6FE7")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 240, 261, 371))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo3.png"))
        self.label_2.setObjectName("label_2")
        self.amountInput = QtWidgets.QLineEdit(self.centralwidget)
        self.amountInput.setGeometry(QtCore.QRect(30, 400, 241, 71))
        font = QtGui.QFont()
        font.setFamily("NewsGoth BT")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.amountInput.setFont(font)
        self.amountInput.setStyleSheet("background-color: #3E6FE7;\n"
"border: 2px solid #3E2FA7;\n"
"border-radius: 22px;\n"
"color: white;")
        self.amountInput.setText("")
        self.amountInput.setAlignment(QtCore.Qt.AlignCenter)
        self.amountInput.setObjectName("amountInput")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 650, 401, 131))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: #3E6FE7;\n"
"border: 2px solid #3E2FA7;\n"
"border-radius: 22px;\n"
"color: white;\n"
"}\n"
"QPushButton: pressed{\n"
"    background_color: #330099\n"
"}\n"
"\n"
"*:hover{\n"
"            background: \'#4663AB\n"
"\';\n"
"        }")
        self.pushButton.setObjectName("pushButton")
       
        self.currencyInput = QtWidgets.QLineEdit(self.centralwidget)
        self.currencyInput.setGeometry(QtCore.QRect(30, 520, 241, 71))
        font = QtGui.QFont()
        font.setFamily("NewsGoth BT")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.currencyInput.setFont(font)
        self.currencyInput.setStyleSheet("background-color: #3E6FE7;\n"
"border: 2px solid #3E2FA7;\n"
"border-radius: 22px;\n"
"color: white;")
        self.currencyInput.setText("")
        self.currencyInput.setAlignment(QtCore.Qt.AlignCenter)
        self.currencyInput.setObjectName("currencyInput")
        self.amountOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.amountOutput.setGeometry(QtCore.QRect(640, 400, 241, 71))
        font = QtGui.QFont()
        font.setFamily("NewsGoth BT")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.amountOutput.setFont(font)
        self.amountOutput.setStyleSheet("background-color: #3E6FE7;\n"
"border: 2px solid #3E2FA7;\n"
"border-radius: 22px;\n"
"color: white;")
        self.amountOutput.setText("")
        self.amountOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.amountOutput.setObjectName("amountOutput")
        self.currencyOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.currencyOutput.setGeometry(QtCore.QRect(640, 520, 241, 71))
        font = QtGui.QFont()
        font.setFamily("NewsGoth BT")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.currencyOutput.setFont(font)
        self.currencyOutput.setStyleSheet("background-color: #3E6FE7;\n"
"border: 2px solid #3E2FA7;\n"
"border-radius: 22px;\n"
"color: white;")
        self.currencyOutput.setText("")
        self.currencyOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.currencyOutput.setObjectName("currencyOutput")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter by Oreh"))
        self.label.setText(_translate("MainWindow", "Currency Converter"))
        self.pushButton.setText(_translate("MainWindow", "Click to Convert"))
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
