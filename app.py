from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dados do currículo
    curriculum = {
        "nome": "David Correia da Silva",
        "curso": "Ciência da Computação - 4º Semestre",
        "habilidades": ["Python", "C/C++", "Arduino", "Inglês"],
        "experiencia": [
            "Estágio como Tutor de TI em Escola de Programação para Crianças",
            "Assistente de Cartão em uma Loja"
        ],
        "idade": 19
    }
    return render_template('port2.html', curriculum=curriculum)

if __name__ == '__main__':
    app.run(debug=True)
