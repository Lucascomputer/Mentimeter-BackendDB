from gitwil import app, db
from flask import render_template, request, jsonify
from gitwil.models import Contato

@app.route('/')
def homepage():
    return render_template('index.html')
    user = 'Manin'
    idade = 22
    context = {
        'user': user,
        'idade': idade
    }
    return render_template('index.html', context = context)

@app.route('/contato', methods=['GET','POST'])
def pag():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa':pesquisa})
        print(pesquisa)

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato=Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            contato=mensagem,
            respondido=1
        )
        db.session.add(contato)
        db.session.commit()

    return render_template('contato.html', context = context)

respostas = []
@app.route('/resposta', methods=['POST'])
def receber_resposta():
    data = request.get_json()
    resposta = data.get('resposta')
    print("Resposta recebida:", resposta)
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip not in respostas:
        respostas.append(ip)
    else:
        return jsonify({"mensagem" :"Resposta não registrada, você já respondeu {}".format(resposta)})
    return jsonify({'mensagem': f'Recebido: {resposta}'})