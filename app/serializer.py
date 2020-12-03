from flask_marshmallow import Marshmallow
from .model import Telecon


ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class TeleconSchema(ma.SQLAlchemyAutoSchema):
    '''
        Classe responsavel por serializar o modelo
        Telecon().
    '''
    class Meta:
        model = Telecon
        