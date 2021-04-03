import sys
import os.path
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from GUI import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):

        super(mywindow, self).__init__()
        self.Your_Balance = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.setWindowTitle('MyFinance')

    def initUI(self):
        self.ui.lineEdit.setText(str(self.Your_Balance))
        self.ui.Income_Button.clicked.connect(self.on_click_add)
        self.ui.Expense_Button.clicked.connect(self.on_click_sub)
        self.show()

        self.ui.tableWidget.update()
        self.ui.lineEdit.update()
        self.ui.lineEdit_2.update()

        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())

        if os.path.exists('Journal.txt'):  # True
            with open('Journal.txt', 'r') as r:
                for i in r:
                    line = i.split()
                    rowPosition = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(rowPosition)
                    self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(line[0]))
                    self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(line[1]))
                    self.ui.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(line[2]))
                    if line[0] == 'Income':
                        self.Your_Balance += int(line[1])
                    elif line[0] == 'Expense':
                        self.Your_Balance -= int(line[1])
        else:
            pass
        self.ui.lineEdit.setText(str(self.Your_Balance))

    #@pyqtSlot()
    def on_click_add(self):
        self.value = self.ui.lineEdit_2.text()
        if self.value == '':
            QMessageBox.warning(self,'Attention!','Enter value!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.Your_Balance += int(self.value)
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit.setText(str(self.Your_Balance))

            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem("Income"))
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(self.value))
            self.ui.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(self.ui.dateEdit.text()))
            with open('Journal.txt', 'a') as a:
                a.write("Income" + ' ' + self.value + ' ' + self.ui.dateEdit.text() + '\n')

    #@pyqtSlot()
    def on_click_sub(self):
        self.value = self.ui.lineEdit_2.text()
        if self.value == '':
            QMessageBox.warning(self,'Attention!', 'Enter value!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.Your_Balance -= int(self.value)
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit.setText(str(self.Your_Balance))

            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem("Expense"))
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(self.value))
            self.ui.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(self.ui.dateEdit.text()))
            with open('Journal.txt', 'a') as a:
                a.write("Expense" + ' ' + self.value + ' ' + self.ui.dateEdit.text() + '\n')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    W = mywindow()
    W.show()
    sys.exit(app.exec_())
