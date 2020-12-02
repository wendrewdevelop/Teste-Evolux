from flask import Blueprint, current_app, request, jsonify
from .model import Telecon
from .serializer import TeleconSchema


bp_telecon = Blueprint('telecon', __name__)

@bp_telecon.route('/mostrar', methods=['GET'])
def mostrar():
    """
        docstring
    """
    bs = TeleconSchema(many=True)
    result = Telecon.query.all()

    return bs.jsonify(result), 200


@bp_telecon.route('/deletar/<int:id>', methods=['GET'])
def deletar(id):
    """
        docstring
    """
    Telecon.query.filter(Telecon.id == id).delete()
    current_app.db.session.commit()

    return jsonify('Registro removido!!')


@bp_telecon.route('/modificar/<int:id>', methods=['POST'])
def modificar(id):
    """
        docstring
    """
    ts = TeleconSchema()

    query = Telecon.query.filter(Telecon.id == id)
    query.update(request.json)
    current_app.db.session.commit()

    return ts.jsonify(query.first())


@bp_telecon.route('/inserir', methods=['POST'])
def inserir():
    """
        docstring
    """
    ts = TeleconSchema()

    value = request.json.get('value', '')
    monthyPrice = request.json.get('monthyPrice', '')
    setupPrice = request.json.get('setupPrice', '')
    currency = request.json.get('currency', '')

    telecon = Telecon(value=value, monthyPrice=monthyPrice, setupPrice=setupPrice, currency=currency)

    current_app.db.session.add(telecon)
    current_app.db.session.commit()

    return ts.jsonify(telecon), 201
