from flask_marshmallow import Marshmallow
from .model import Telecon


ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class TeleconSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Telecon
        