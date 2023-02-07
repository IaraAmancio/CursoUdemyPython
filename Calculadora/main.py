from calc import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class App(QMainWindow, Ui_Calculadora):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btn0.clicked.connect(lambda: self.funcao_exibir(self.btn0.text()))

        self.btn1.clicked.connect(lambda: self.funcao_exibir(self.btn1.text()))
        self.btn2.clicked.connect(lambda: self.funcao_exibir(self.btn2.text()))
        self.btn3.clicked.connect(lambda: self.funcao_exibir(self.btn3.text()))

        self.btn4.clicked.connect(lambda: self.funcao_exibir(self.btn4.text()))
        self.btn5.clicked.connect(lambda: self.funcao_exibir(self.btn5.text()))
        self.btn6.clicked.connect(lambda: self.funcao_exibir(self.btn6.text()))

        self.btn7.clicked.connect(lambda: self.funcao_exibir(self.btn7.text()))
        self.btn8.clicked.connect(lambda: self.funcao_exibir(self.btn8.text()))
        self.btn9.clicked.connect(lambda: self.funcao_exibir(self.btn9.text()))

        self.btn_virgula.clicked.connect(lambda : self.funcao_exibir('.'))

        self.btn_porcent.clicked.connect(lambda : self.funcao_exibir(' '+self.btn_porcent.text()+' '))
        self.btn_soma.clicked.connect(lambda: self.funcao_exibir(' '+self.btn_soma.text()+' '))
        self.btn_subtracao.clicked.connect(lambda: self.funcao_exibir(' '+self.btn_subtracao.text()+' '))
        self.btn_multiplicacao.clicked.connect(lambda: self.funcao_exibir(' '+self.btn_multiplicacao.text()+' '))
        self.btn_divisao.clicked.connect(lambda: self.funcao_exibir(' '+self.btn_divisao.text()+' '))

        self.btn_igual.clicked.connect(lambda: self.funcao_eval())

        self.btn_clear.clicked.connect(lambda : self.display.setText(''))
        self.btn_delete.clicked.connect(lambda : self.display.setText(self.display.text()[:-1]))


    def funcao_exibir(self, texto):
        self.display.setText(self.display.text() + texto)

    def funcao_eval(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('ERRO')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()

