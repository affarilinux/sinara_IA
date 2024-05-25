import requests


class Cliente:

    def enviar_pergunta(self, pergunta, porta):
        self.url_base = "http://127.0.0.1:{}/api/resposta"
        self.headers = {"Content-Type": "application/json"}
        url = self.url_base.format(porta)
        data = {"pergunta": pergunta}

        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            resposta = response.json().get('resposta')

        except requests.exceptions.RequestException as e:
            return f"Erro ao se conectar ao servidor: {e.__class__}"

        except Exception as e:
            return f"Erro inesperado: {e}"

        else:
            return resposta


class ClienteLoop:

    loop = True
    acesso = None
    acesso_anterior = None
    porta = None

    def __init__(self):

        self.printar_text()

        while ClienteLoop.loop:

            self.ACESSO()

            self.verificar()

    def verificar(self):
        match ClienteLoop.acesso:

            case 0:
                ClienteLoop.loop = False

            case 1:
                if ClienteLoop.porta is None:
                    print("* apenas números.")
                    porta_2 = input("* Digite a porta do servidor: ")

                    self.porta_acesso_servidor(porta_2)

                print("\n")
                pergunta = input("Digite sua pergunta: ")

                class_api = Cliente()
                resposta = class_api.enviar_pergunta(
                    pergunta, ClienteLoop.porta
                )
                print(resposta)
                print("\n")

            case 2:
                print("* apenas números.")
                porta_2 = input("* Digite a nova porta do servidor: ")
                self.porta_acesso_servidor(porta_2)

    def ACESSO(self):
        try:

            testar = int(input("Digite um número de acesso: "))

        except Exception as er:
            print(f"Erro inesperado, variavel acesso: {er.__class__}")

        else:
            self.printar()

            if testar < 0:
                print("valor menor que zero não funciona")

            elif testar > 5:
                print("valor acima do limite")

            elif ClienteLoop.acesso != testar:

                if (ClienteLoop.acesso is None and
                        ClienteLoop.acesso_anterior is None):

                    ClienteLoop.acesso_anterior = testar
                    ClienteLoop.acesso = testar

                else:
                    if testar == 0:
                        ClienteLoop.acesso = testar

                    else:
                        ClienteLoop.acesso_anterior = testar
                        ClienteLoop.acesso = testar
                        self.printar_text()
                        self.printar()

    def porta_acesso_servidor(self, mudar):
        try:
            numero = int(mudar)

        except Exception as err:
            print(f"Erro inesperado, variavel porta: {err.__class__}")

        else:
            ClienteLoop.porta = numero

    def printar_text(self):
        self.printar()
        print("""
            0 => Sair do loop
            1 => Conversar
            2 => Mudar ou inserir Porta
        """)
        self.printar()

    def printar(self):
        print("#-" * 20)


if __name__ == "__main__":
    tec = ClienteLoop()
