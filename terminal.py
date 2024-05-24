import requests


class Cliente:

    def __init__(self):
        self.url_base = "http://127.0.0.1:{}/api/resposta"  # sem porta de acesso
        self.headers = {"Content-Type": "application/json"}  # tipo leitura

    def enviar_pergunta(self, pergunta, porta):
        url = self.url_base.format(porta)
        data = {"pergunta": pergunta}

        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()

            resposta = response.json().get('resposta')
            return resposta
        except requests.exceptions.RequestException as e:
            return f"Erro ao se conectar ao servidor: {e}"


class ClienteLoop:

    loop = True
    acesso = None
    acesso_anterior = None

    porta = None

    def __init__(self):
        super().__init__()

        while ClienteLoop.loop == True:

            if (ClienteLoop.acesso_anterior !=
                    ClienteLoop.acesso
                ):

                self.printar()

                print(
                    """
                    0 => Sair do loop\n
                    1 => Conversar\n
                    2 => Mudar ou inserir Porta
                    """)
                self.printar()

            self.verificar()

    def verificar(self):

        match ClienteLoop.acesso:

            case 0:

                ClienteLoop.loop = False
             # Captura qualquer outra exceção não esperada

            case 1:

                if ClienteLoop.porta == None:

                    print("* apenas números.")
                    porta_2 = input("Digite a porta do servidor: ")

                    self.porta_acesso_servidor(porta_2)

                pergunta = input("Digite sua pergunta: ")

                class_api = Cliente()
                resposta = class_api.enviar_pergunta(
                    pergunta, ClienteLoop.porta
                )
                print(resposta)
            case _:

                try:

                    testar = int(ClienteLoop.acesso)

                    if testar < 0:

                        print("valor menor que zero não funciona")

                    elif testar > 5:

                        print("valor acima do limite")

                except Exception as er:
                    # Captura qualquer exceção não esperada
                    return f"Erro inesperado, variavel acesso: {er}"

    def porta_acesso_servidor(self, mudar):

        try:

            numero = int(mudar)

            ClienteLoop.porta = numero

        except Exception as err:
            # Captura qualquer exceção não esperada
            return f"Erro inesperado, variavel porta: {err}"

    def printar(self):

        print("#-"*20)
        print("\n")


if __name__ == "__main__":

    tec = ClienteLoop()
