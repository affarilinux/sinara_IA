from BANCO.tabela import Tabela

from SEGURANCA.celula import Celula

from API.teclado.entrada import APITecladoEntrada


class Segunca:

    # criar tabela
    tabela = Tabela()
    tabela.Criar_verificar_tab()

    # tabela celular
    cellular = Celula()
    cellular.ver_celula()

    apitecla = APITecladoEntrada()
    apitecla.run()
    print(12)
