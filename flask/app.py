from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SECRET_KEY'] = 'UEUEHUEHEUHEUH'


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
    coluna_pesquisa = request.form.get('Colunas')
    texto_pesquisa = request.form.get('TextoProcurar')

    if coluna_pesquisa == 'DESCRICAO':
        products = produtos.query.filter(produtos.DESCRICAO.like(f"%{texto_pesquisa}%")).all()
    elif coluna_pesquisa == 'COD':
        products = produtos.query.filter(produtos.CODIGO.like(f"%{texto_pesquisa}%")).all()
    else:
        products = []

    return render_template('retorno.html', products=products)



@app.route('/update_stock', methods=['POST'])
def update_stock():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity'))

    product = produtos.query.get(product_id)
    if product:
        product.QUANTIDADE += quantity
        db.session.commit()
        flash(f'Estoque atualizado para {product.QUANTIDADE} unidades.', 'success')
    else:
        flash('Produto não encontrado', 'error')

    return redirect(url_for('search'))


if __name__ == '__main__':
    app.run(debug=True)