from BANCO.base import Base


class Celula(Base):

    def ver_celula(self):

        self.ativar_banco()

        ver = ("TABELA", 100)

        # Consulta SQL para selecionar a célula
        consulta = '''
        SELECT celula, sinapse FROM Tab_celula
        WHERE celula = ?
        '''

        # Executa a consulta
        self.cursorsq.execute(consulta, (ver[0],))

        # Recupera os resultados da consulta
        cell = self.cursorsq.fetchall()

        # Se não houver resultados, insere os dados
        if not cell:
            inserir = "INSERT INTO Tab_celula (celula, sinapse) VALUES (?, ?)"

            # Executa a inserção
            self.cursorsq.execute(inserir, (ver[0], ver[1]))

        self.commit_banco()
        self.sair_banco()
