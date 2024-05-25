from BANCO.base import Base


class Caractere(Base):

    def Verificar_caractere(self, frase):

        for caracterefs in frase:

            vr_caract = self.banco_caractere(caracterefs)

            # print(vr_caract)
            if len(vr_caract) == 0:

                print(vr_caract)

    def banco_caractere(self, caractfs):
        self.ativar_banco()

        consulta_ct = '''
        SELECT caractere FROM Tab_tecla
        WHERE caractere = ?
        '''

        # Executa a consulta
        self.cursorsq.execute(consulta_ct, (caractfs,))
        results = self.cursorsq.fetchall()

        # returna uma lista- nao aceita retornar[0]
        return results

        self.sair_banco()
