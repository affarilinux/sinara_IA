from BANCO.base import Base


class CaractereAtual(Base):

    def inserir_db_caractere(self, carac):

    def Tab_teclado_entrada(self):

    Tab_teclado_entrada

    def Tab_tecla_insert(carac, lista):

        self.ativar_banco()

        consulta_in = '''
            INSERT INTO Tab_tecla( caractere, lista_teclado)
            VALUE (?,?)
            '''

        # Executa a consulta
        self.cursorsq.execute(consulta_in, (carac, lista))
        results = self.cursorsq.fetchall()

        self.commit_banco()
        self.sair_banco()
