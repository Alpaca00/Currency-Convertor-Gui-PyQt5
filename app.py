#! /usr/bin/python3.8
import sys
import json
import urllib.request
import style
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


try:
    html = urllib.request.urlopen('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    data = html.read()
    JSON_object = json.loads(data)
except ReferenceError as err:
    print(f'Warning! {err}')


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сurrency Сonverter')
        self.setGeometry(450, 150, 370, 450)
        self.setStyleSheet('background-color: #0095D0;')
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('icons/world.ico'))
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
        self.displayCurrency()
        self.updatedCurrencyRates()

    def widgets(self):
        ########widgets of top layout########
        self.titleImg = QLabel()
        self.img = QPixmap('icons/bitcoin.png')
        self.titleImg.setPixmap(self.img)
        self.titleImg.setToolTip('Data provided by PrivatBank (for currency) and PrivatBank (for cryptocurrency)')
        self.titleImg.setStyleSheet(style.toolTipStyle())
        self.allCurrencyDisplay = QLabel()
        self.usdLabel = QLabel()
        self.eurLabel = QLabel()
        self.rubLabel = QLabel()
        self.btcLabel = QLabel()
        #######widgets of middle layout#######
        self.amountLineEdit = QLineEdit()
        self.amountLineEdit.setPlaceholderText('Enter your amount to convert')
        self.amountLineEdit.setStyleSheet(style.lineEditStyle())
        self.fromComboCurrency = QComboBox()
        self.fromComboCurrency.addItems(
            ['United States USD', 'Europe EURO', 'Russia RUBLE', 'Cryptocurrency BITCOIN', 'Ukraine UAH'])
        self.fromComboCurrency.setStyleSheet(style.textStyle())
        self.toComboCurrency = QComboBox()
        self.toComboCurrency.addItems(
            ['Ukraine UAH', 'Cryptocurrency BITCOIN', 'Russia RUBLE', 'Europe EURO', 'United States USD'])
        self.toComboCurrency.setStyleSheet(style.textStyle())
        self.amountText = QLabel('Amount: ')
        self.amountText.setStyleSheet(style.textLabelstyle())
        self.fromText = QLabel('From: ')
        self.fromText.setStyleSheet(style.textLabelstyle())
        self.toText = QLabel('To: ')
        self.toText.setStyleSheet(style.textLabelstyle())
        self.resultBtn = QPushButton('Result')
        self.resultBtn.setStyleSheet(style.resultBtnStyle())
        self.resultBtn.clicked.connect(self.confirmOperation)
        self.resultLabel = QLabel()
        self.resultLabel.setStyleSheet(style.resultLabelStyle())
        ########widget of bottom layout######
        self.latestCurrencyRates = QLabel()

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.middleLayout = QFormLayout()
        self.bottomLayout = QHBoxLayout()
        self.topFrame = QFrame()
        self.middleFrame = QFrame()
        self.bottomFrame = QFrame()
        #######Add widgets of top layout######
        self.topLayout.addWidget(self.titleImg)
        self.topLayout.addWidget(self.allCurrencyDisplay)
        self.topLayout.addWidget(self.usdLabel)
        self.topLayout.addWidget(self.eurLabel)
        self.topLayout.addWidget(self.rubLabel)
        self.topLayout.addWidget(self.btcLabel)
        self.topFrame.setLayout(self.topLayout)
        self.topLayout.setSpacing(1)
        ########Add widgets of middle layout####
        self.middleLayout.addRow(self.amountText, self.amountLineEdit)
        self.middleLayout.addRow(self.fromText, self.fromComboCurrency)
        self.middleLayout.addRow(self.toText, self.toComboCurrency)
        self.middleLayout.addRow(QLabel(''), self.resultLabel)
        self.middleLayout.addRow(QLabel(''), self.resultBtn)
        self.middleFrame.setLayout(self.middleLayout)
        #########Add widgets of bottom layout########
        self.bottomLayout.addWidget(QLabel('Latest currency rates'))
        self.bottomLayout.addStretch()
        self.bottomLayout.addWidget(self.latestCurrencyRates)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame, 45)
        self.mainLayout.addWidget(self.middleFrame, 45)
        self.mainLayout.addWidget(self.bottomFrame, 10)
        self.setLayout(self.mainLayout)

    def displayCurrency(self):
        global JSON_object
        global usdBuy, usdSale, eurBuy, eurSale, rubBuy, rubSale, btcBuy, btcSale
        self.allCurrencyDisplay.setText('Currency ' + '\t' + ' Buy ' + '\t' + ' Sale')
        self.allCurrencyDisplay.setAlignment(Qt.AlignLeft)
        self.allCurrencyDisplay.setStyleSheet(style.displayStyle())
        usdBuy = JSON_object[0]['buy']
        buyUsd = round(float(usdBuy), 2)
        usdSale = JSON_object[0]['sale']
        saleUsd = round(float(usdSale), 2)
        self.usdLabel.setText('USD' + '\t\t' + str(buyUsd) + '\t' + str(saleUsd))
        self.usdLabel.setAlignment(Qt.AlignLeft)
        self.usdLabel.setStyleSheet(style.displayStyle())
        eurBuy = JSON_object[1]['buy']
        buyEur = round(float(eurBuy), 2)
        eurSale = JSON_object[1]['sale']
        saleEur = round(float(eurSale), 2)
        self.eurLabel.setText('EUR' + '\t\t' + str(buyEur) + '\t' + str(saleEur))
        self.eurLabel.setAlignment(Qt.AlignLeft)
        self.eurLabel.setStyleSheet(style.displayStyle())
        rubBuy = JSON_object[2]['buy']
        buyRub = round(float(rubBuy), 3)
        rubSale = JSON_object[2]['sale']
        saleRub = round(float(rubSale), 3)
        self.rubLabel.setText('RUB' + '\t\t' + str(buyRub) + '\t' + str(saleRub))
        self.rubLabel.setAlignment(Qt.AlignLeft)
        self.rubLabel.setStyleSheet(style.displayStyle())
        btcBuy = JSON_object[3]['buy']
        buyBtc = round(float(btcBuy), 2)
        btcSale = JSON_object[3]['sale']
        saleBtc = round(float(btcSale), 2)
        self.btcLabel.setText('BTC' + '\t\t' + str(buyBtc) + ' ' + str(saleBtc))
        self.btcLabel.setAlignment(Qt.AlignLeft)
        self.btcLabel.setStyleSheet(style.displayStyle())

    def confirmOperation(self):
        global JSON_object
        global usdBuy, usdSale, eurBuy, eurSale, rubBuy, rubSale, btcBuy, btcSale
        valueFrom = self.fromComboCurrency.currentText()
        valueTo = self.toComboCurrency.currentText()
        amount = self.amountLineEdit.text()
        try:
            if (valueFrom == 'United States USD') and (valueTo == 'Ukraine UAH'):
                calculation = float(usdBuy) * float(amount)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' USD' + '\t' + str(calculation) + ' UAH')
            elif (valueFrom == 'Europe EURO') and (valueTo == 'Ukraine UAH'):
                calculation = float(eurBuy) * float(amount)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' EURO' + '\t' + str(calculation) + ' UAH')
            elif (valueFrom == 'Russia RUBLE') and (valueTo == 'Ukraine UAH'):
                calculation = float(rubBuy) * float(amount)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' RUB' + '\t' + str(calculation) + ' UAH')
            elif (valueFrom == 'Cryptocurrency BITCOIN') and (valueTo == 'Ukraine UAH'):
                calculation = float(btcBuy) * (float(amount) * float(usdBuy))
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' BTC' + '\t' + str(calculation) + ' UAH')
            elif (valueFrom == 'Ukraine UAH') and (valueTo == 'Ukraine UAH'):
                self.resultLabel.setText(str(amount) + ' UAH')
            elif (valueFrom == 'United States USD') and (valueTo == 'United States USD'):
                self.resultLabel.setText(str(amount) + ' USD')
            elif (valueFrom == 'Europe EURO') and (valueTo == 'Europe EURO'):
                self.resultLabel.setText(str(amount) + ' EURO')
            elif (valueFrom == 'Russia RUBLE') and (valueTo == 'Russia RUBLE'):
                self.resultLabel.setText(str(amount) + ' RUB')
            elif (valueFrom == 'Cryptocurrency BITCOIN') and (valueTo == 'Cryptocurrency BITCOIN'):
                self.resultLabel.setText(str(amount) + ' BTC')
            elif (valueFrom == 'Ukraine UAH') and (valueTo == 'United States USD'):
                calculation = float(amount) / float(usdSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' UAH' + '\t' + str(calculation) + ' USD')
            elif (valueFrom == 'Ukraine UAH') and (valueTo == 'Europe EURO'):
                calculation = float(amount) / float(eurSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' UAH' + '\t' + str(calculation) + ' EURO')
            elif (valueFrom == 'Ukraine UAH') and (valueTo == 'Russia RUBLE'):
                calculation = float(amount) / float(rubSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' UAH' + '\t' + str(calculation) + ' RUB')
            elif (valueFrom == 'Ukraine UAH') and (valueTo == 'Cryptocurrency BITCOIN'):
                calculation = float(amount) / float(btcSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' UAH' + '\t' + str(calculation) + ' BTC')
            elif (valueFrom == 'United States USD') and (valueTo == 'Europe EURO'):
                calculation = float(usdBuy) * float(amount) / float(eurSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' USD' + '\t' + str(calculation) + ' EURO')
            elif (valueFrom == 'United States USD') and (valueTo == 'Russia RUBLE'):
                calculation = float(usdBuy) * float(amount) / float(rubSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' USD' + '\t' + str(calculation) + ' RUB')
            elif (valueFrom == 'United States USD') and (valueTo == 'Cryptocurrency BITCOIN'):
                calculation = float(amount) / float(btcSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' USD' + '\t' + str(calculation) + ' BTC')
            elif (valueFrom == 'Europe EURO') and (valueTo == 'United States USD'):
                calculation = float(eurBuy) * float(amount) / float(usdSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' EURO' + '\t' + str(calculation) + ' USD')
            elif (valueFrom == 'Europe EURO') and (valueTo == 'Russia RUBLE'):
                calculation = float(eurBuy) * float(amount) / float(rubSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' EURO' + '\t' + str(calculation) + ' RUB')
            elif (valueFrom == 'Europe EURO') and (valueTo == 'Cryptocurrency BITCOIN'):
                fromEurToUsd = (float(eurBuy) * float(amount) / float(usdSale))
                calculation = float(fromEurToUsd) / float(btcSale)
                self.resultLabel.setText(str(amount) + ' EURO' + '\t' + str(calculation) + ' BTC')
            elif (valueFrom == 'Russia RUBLE') and (valueTo == 'United States USD'):
                calculation = float(rubBuy) * float(amount) / float(usdSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' RUB' + '\t' + str(calculation) + ' USD')
            elif (valueFrom == 'Russia RUBLE') and (valueTo == 'Europe EURO'):
                calculation = float(rubBuy) * float(amount) / float(usdSale)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' RUB' + '\t' + str(calculation) + ' EURO')
            elif (valueFrom == 'Russia RUBLE') and (valueTo == 'Cryptocurrency BITCOIN'):
                fromEurToUsd = (float(rubBuy) * float(amount) / float(usdSale))
                calculation = float(fromEurToUsd) / float(btcSale)
                self.resultLabel.setText(str(amount) + ' RUB' + '\t' + str(calculation) + ' BTC')
            elif (valueFrom == 'Cryptocurrency BITCOIN') and (valueTo == 'United States USD'):
                calculation = float(btcBuy) * float(amount)
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' BTC' + '\t' + str(calculation) + ' USD')
            elif (valueFrom == 'Cryptocurrency BITCOIN') and (valueTo == 'Europe EURO'):
                calculation = float(btcBuy) * float(amount)
                calculation = calculation / (float(eurBuy) * float(amount) / float(usdSale))
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' BTC' + '\t' + str(calculation) + ' EURO')
            elif (valueFrom == 'Cryptocurrency BITCOIN') and (valueTo == 'Russia RUBLE'):
                calculation = float(btcBuy) * float(amount)
                calculation = calculation / (float(rubBuy) * float(amount) / float(usdSale))
                calculation = round(calculation, 2)
                self.resultLabel.setText(str(amount) + ' BTC' + '\t' + str(calculation) + ' RUB')
            else:
                QMessageBox.information(self, 'Warning', 'Amount line cant be empty!')
        except:
            QMessageBox.information(self, 'Info', 'Something went wrong')

    def updatedCurrencyRates(self):
        current_time = datetime.now()
        current = current_time.strftime("%d-%m-%Y %H:%M")
        self.latestCurrencyRates.setText(str(current))


def main():
    APP = QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())


if __name__ == '__main__':
    main()
