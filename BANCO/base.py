import sqlite3


class Base:

    def ativar_banco(self):
        self.bancovar = sqlite3.connect('BANCO/Sinara.db')
        self.cursorsq = self.bancovar.cursor()

    def commit_banco(self):
        self.bancovar.commit()

    def sair_banco(self):
        self.cursorsq.close()
        self.bancovar.close()
