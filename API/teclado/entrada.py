from flask import Flask, request, jsonify


class APITecladoEntrada:

    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/api/resposta', methods=['POST'])
        def receber_resposta():
            data = request.json
            resposta = self.processar_requisicao(data)
            return jsonify({'resposta': resposta})

    def processar_requisicao(self, data):
        # Aqui você pode adicionar sua lógica para processar a requisição e gerar uma resposta
        pergunta = data.get('pergunta')
        resposta = f'Você perguntou: {pergunta}. Esta é a resposta.'
        return resposta

    def run(self):
        self.app.run(debug=True)
