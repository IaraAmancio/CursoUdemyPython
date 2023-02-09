from valida_gera_cpf import *
from design import *
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

class valida_gera_cpf(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btn_validar.clicked.connect(lambda : self.action_btn_validar())
        self.btn_gerar.clicked.connect(lambda : self.action_btn_gerar())

    def action_btn_validar(self):
        if funcValidarCPF(self.input_valida.text()):
            self.input_display.setText('CPF válido!')
        else:
            self.input_display.setText('CPF inválido!')

    def action_btn_gerar(self):
        self.input_valida.setText('')
        self.input_display.setText(funcGerarCPF())

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = valida_gera_cpf()
    app.show()
    qt.exec_()


