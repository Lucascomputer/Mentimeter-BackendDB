from flask import Flask, request, jsonify

app = Flask(__name__)

respostas = []
@app.route('/resposta', methods=['POST'])
def receber_resposta():
    data = request.get_json()
    resposta = data.get('resposta')
    print("Resposta recebida:", resposta)
    ip = request.remote_addr
    if ip not in respostas:
        respostas.append(ip)
    else:
        return jsonify({"mensagem" :"Resposta não registrada, você já respondeu {}".format(resposta)})
    return jsonify({'mensagem': f'Recebido: {resposta}'})

if __name__ == '__main__':
    app.run(debug=True)
