from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db


class Telecon(db.Model):
    '''
        Classe que abstrai o modelo Telecon,
        utilizando a lib flask_sqlalchemy para
        fazer essa tradução.
    '''
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255))
    monthyPrice = db.Column(db.Float)
    setupPrice = db.Column(db.Float)
    currency = db.Column(db.String(255))