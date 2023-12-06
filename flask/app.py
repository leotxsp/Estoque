from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)

class produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CODIGO = db.Column(db.String(10))
    DESCRICAO = db.Column(db.String(255))
    NCM = db.Column(db.String(20))
    VALOR_SAIDA = db.Column(db.Float)
    QUANTIDADE = db.Column(db.Integer)

    @property
    def VALOR_FORMATADO(self):
        return 'R$ {:.2f}'.format(self.VALOR_SAIDA)

@app.route('/pecas')
def pecas():

    return render_template('pecas.html',)

@app.route('/')
def index():
    return render_template('index.html')

  

@app.route('/search', methods=['POST', 'GET'])
def search():
    coluna_pesquisa = request.form['Colunas']
    texto_pesquisa = request.form['TextoProcurar']
    print(coluna_pesquisa,texto_pesquisa)
    if coluna_pesquisa == 'DESCRICAO':
            products = produtos.query.filter(produtos.DESCRICAO.like(f"%{texto_pesquisa}%")).all()

            return render_template('retorno.html', products=products)
    elif coluna_pesquisa == 'COD':
            products = produtos.query.filter(produtos.CODIGO.like(f"%{texto_pesquisa}%")).all()

            return render_template('retorno.html', products=products)
    
    print(coluna_pesquisa,texto_pesquisa)

    
        
   
    return render_template('retorno.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)