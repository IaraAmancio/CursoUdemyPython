# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        Calculadora.setObjectName("Calculadora")
        Calculadora.resize(400, 420)
        Calculadora.setMinimumSize(QtCore.QSize(400, 400))
        Calculadora.setMaximumSize(QtCore.QSize(400, 420))
        Calculadora.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(Calculadora)
        self.centralwidget.setObjectName("centralwidget")
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setEnabled(False)
        self.display.setGeometry(QtCore.QRect(10, 10, 380, 80))
        self.display.setMinimumSize(QtCore.QSize(380, 80))
        self.display.setMaximumSize(QtCore.QSize(380, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.display.setFont(font)
        self.display.setMouseTracking(False)
        self.display.setText("")
        self.display.setReadOnly(False)
        self.display.setClearButtonEnabled(False)
        self.display.setObjectName("display")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(9, 107, 65, 65))
        self.btn7.setMinimumSize(QtCore.QSize(65, 65))
        self.btn7.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(88, 107, 65, 65))
        self.btn8.setMinimumSize(QtCore.QSize(65, 65))
        self.btn8.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(165, 107, 65, 65))
        self.btn9.setMinimumSize(QtCore.QSize(65, 65))
        self.btn9.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(9, 184, 65, 65))
        self.btn4.setMinimumSize(QtCore.QSize(65, 65))
        self.btn4.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(88, 184, 65, 65))
        self.btn5.setMinimumSize(QtCore.QSize(65, 65))
        self.btn5.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(165, 184, 65, 65))
        self.btn6.setMinimumSize(QtCore.QSize(65, 65))
        self.btn6.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(9, 261, 65, 65))
        self.btn1.setMinimumSize(QtCore.QSize(65, 65))
        self.btn1.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(88, 261, 65, 65))
        self.btn2.setMinimumSize(QtCore.QSize(65, 65))
        self.btn2.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(165, 261, 65, 65))
        self.btn3.setMinimumSize(QtCore.QSize(65, 65))
        self.btn3.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn_porcent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_porcent.setGeometry(QtCore.QRect(9, 338, 65, 65))
        self.btn_porcent.setMinimumSize(QtCore.QSize(65, 65))
        self.btn_porcent.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_porcent.setFont(font)
        self.btn_porcent.setObjectName("btn_porcent")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(88, 338, 65, 65))
        self.btn0.setMinimumSize(QtCore.QSize(65, 65))
        self.btn0.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.btn_virgula = QtWidgets.QPushButton(self.centralwidget)
        self.btn_virgula.setGeometry(QtCore.QRect(165, 338, 65, 65))
        self.btn_virgula.setMinimumSize(QtCore.QSize(65, 65))
        self.btn_virgula.setMaximumSize(QtCore.QSize(65, 65))
        self.btn_virgula.setObjectName("btn_virgula")
        self.btn_soma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_soma.setGeometry(QtCore.QRect(242, 107, 65, 65))
        self.btn_soma.setMinimumSize(QtCore.QSize(65, 65))
        self.btn_soma.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_soma.setFont(font)
        self.btn_soma.setObjectName("btn_soma")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(319, 107, 65, 65))
        self.btn_clear.setMinimumSize(QtCore.QSize(65, 65))
        self.btn_clear.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.btn_subtracao = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subtracao.setGeometry(QtCore.QRect(242, 184, 65, 65))
        self.btn_subtracao.setMinimumSize(QtCore.QSize(65, 65))
        self.btn_subtracao.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_subtracao.setFont(font)
        self.btn_subtracao.setObjectName("btn_subtracao")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(319, 184, 65, 65))
        self.btn_delete.setMinimumSize(QtCore.QSize(65, 65))
        self.btn_delete.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_multiplicacao = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiplicacao.setGeometry(QtCore.QRect(242, 261, 65, 65))
        self.btn_multiplicacao.setMinimumSize(QtCore.QSize(65, 65))
        self.btn_multiplicacao.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_multiplicacao.setFont(font)
        self.btn_multiplicacao.setObjectName("btn_multiplicacao")
        self.btn_igual = QtWidgets.QPushButton(self.centralwidget)
        self.btn_igual.setGeometry(QtCore.QRect(319, 260, 65, 140))
        self.btn_igual.setMinimumSize(QtCore.QSize(65, 140))
        self.btn_igual.setMaximumSize(QtCore.QSize(65, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_igual.setFont(font)
        self.btn_igual.setObjectName("btn_igual")
        self.btn_divisao = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divisao.setGeometry(QtCore.QRect(242, 338, 65, 65))
        self.btn_divisao.setMinimumSize(QtCore.QSize(65, 65))
        self.btn_divisao.setMaximumSize(QtCore.QSize(65, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_divisao.setFont(font)
        self.btn_divisao.setObjectName("btn_divisao")
        Calculadora.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculadora)
        QtCore.QMetaObject.connectSlotsByName(Calculadora)

    def retranslateUi(self, Calculadora):
        _translate = QtCore.QCoreApplication.translate
        Calculadora.setWindowTitle(_translate("Calculadora", "Calculadora"))
        self.btn7.setText(_translate("Calculadora", "7"))
        self.btn8.setText(_translate("Calculadora", "8"))
        self.btn9.setText(_translate("Calculadora", "9"))
        self.btn4.setText(_translate("Calculadora", "4"))
        self.btn5.setText(_translate("Calculadora", "5"))
        self.btn6.setText(_translate("Calculadora", "6"))
        self.btn1.setText(_translate("Calculadora", "1"))
        self.btn2.setText(_translate("Calculadora", "2"))
        self.btn3.setText(_translate("Calculadora", "3"))
        self.btn_porcent.setText(_translate("Calculadora", "%"))
        self.btn0.setText(_translate("Calculadora", "0"))
        self.btn_virgula.setText(_translate("Calculadora", ","))
        self.btn_soma.setText(_translate("Calculadora", "+"))
        self.btn_clear.setText(_translate("Calculadora", "Clear"))
        self.btn_subtracao.setText(_translate("Calculadora", "-"))
        self.btn_delete.setText(_translate("Calculadora", "<-"))
        self.btn_multiplicacao.setText(_translate("Calculadora", "*"))
        self.btn_igual.setText(_translate("Calculadora", "="))
        self.btn_divisao.setText(_translate("Calculadora", "/"))
