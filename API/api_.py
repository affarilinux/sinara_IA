from flask import Flask, request, jsonify

from API.teclado.caractere import Caractere


class APITecladoEntrada:

    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        # so no momento da request a funcao e ativada
        @self.app.route('/api/resposta', methods=['POST'])
        def receber_resposta():

            # pega a frase do http e transforma em dicionario
            data = request.json
            # processa na função
            resposta = self.processar_requisicao(data)
            # leva de volta ao cliente
            return jsonify({'resposta': resposta})

    def processar_requisicao(self, data):

        # Aqui você pode adicionar sua lógica para processar a requisição e gerar uma resposta
        pergunta = data.get('pergunta')

        # api/teclado.caractere
        caract = Caractere()
        caract.Verificar_caractere(str(pergunta))

        resposta = f'Você perguntou: {pergunta}. Esta é a resposta.'
        return resposta

    def run(self):
        self.app.run(debug=True)
