# You need to type currencies in UPPERCASE e.g. USD etc, otherwise the code won't work.
# It has a number of bugs so far that will be corrected soon


from email.mime import application
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter


def main():

    class CurrencyConv(QtWidgets.QMainWindow):
        def __init__(self):
            super(CurrencyConv, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.init_UI()

        def init_UI(self):
            self.setWindowIcon(QIcon("logo3.png"))
            self.ui.amountInput.setPlaceholderText("I have now")
            self.ui.currencyInput.setPlaceholderText("In currency")
            self.ui.amountOutput.setPlaceholderText("I will get")
            self.ui.currencyOutput.setPlaceholderText("In currency")
            self.ui.pushButton.clicked.connect(self.converter)

        def converter(self):
            c = CurrencyConverter()
            input_currency = self.ui.currencyInput.text()
            output_currency = self.ui.currencyOutput.text()
            input_amount = int(self.ui.amountInput.text())

            output_amount = round(c.convert(input_amount, '%s' % (
                input_currency), '%s' % (output_currency)), 2)

            self.ui.amountOutput.setText(str(output_amount))

    app = QtWidgets.QApplication([])
    application = CurrencyConv()
    application.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
