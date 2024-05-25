
from BANCO.base import Base


class Tabela(Base):

    def Criar_verificar_tab(self):

        # ESTRUTURA
        self.ativar_banco()

        self.cursorsq.execute(
            """CREATE TABLE if not exists Tab_celula(
            
                ID_Celula INTEGER PRIMARY KEY AUTOINCREMENT,
                
                celula  TEXT,
                sinapse INT
                
                )""")
        self.commit_banco()
        self.sair_banco()

        # TECLADO
        self.ativar_banco()

        # peso = 24 horas reduz 0.009 ponto, cada chamado + 0.001
        # carga = pico ou repouso de carga
        self.cursorsq.execute(
            """CREATE TABLE if not exists Tab_teclado_entrada(
            
                ID_Teclado INTEGER PRIMARY KEY AUTOINCREMENT,
                
                peso     INT,
                carga    INT,

                source_id  INT,
                conexoes   INT,
                target_id  INT,

                FOREIGN KEY (source_id) REFERENCES Tab_celula(ID_Celula),
                FOREIGN KEY (target_id) REFERENCES Tab_celula(ID_Celula)

                )""")

        # lista_teclado TEXT <= ID_Teclado
        self.cursorsq.execute(
            """CREATE TABLE if not exists Tab_tecla(
            
                ID_Tecla INTEGER PRIMARY KEY AUTOINCREMENT,
                
                caractere TEXT,
                lista_teclado TEXT
                
                )""")

        self.commit_banco()
        self.sair_banco()
