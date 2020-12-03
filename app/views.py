from flask import Blueprint, current_app, request, jsonify
from .model import Telecon
from .serializer import TeleconSchema


bp_telecon = Blueprint('telecon', __name__)

@bp_telecon.route('/mostrar', methods=['GET'])
def mostrar():
    """
        Função que retorna os registros do modelo Telecon()
        para a endpoint. 

        Só o metodo GET é permitido.

        Endpoint: /mostrar
    """
    bs = TeleconSchema(many=True)
    result = Telecon.query.all()

    return bs.jsonify(result), 200


@bp_telecon.route('/detail/<int:id>', methods=['GET'])
def detail(id):
    """
        Função que retorna um registro especifica 
        do modelo Telecon() para a endpoint. 

        Só o metodo GET é permitido.

        Endpoint: /detail/<int:id>
    """
    bs = TeleconSchema()
    result = Telecon.query.get(id)

    return bs.jsonify(result), 200


@bp_telecon.route('/deletar/<int:id>', methods=['GET'])
def deletar(id):
    """
        Função responsavel por excluir um registro da base
        de dados, com base no identificador passado como 
        parametro na URL. 

        Só o metodo GET é permitido.

        Endpoint: /deletar/<int:id>
        Identiicador: id
    """
    Telecon.query.filter(Telecon.id == id).delete()
    current_app.db.session.commit()

    return jsonify('Registro removido!!')


@bp_telecon.route('/modificar/<int:id>', methods=['POST'])
def modificar(id):
    """
        Função responsavel por atualizar os dados do registro
        com base no identificador fornecido pelo usuario. 

        O metodo POST é utilizado nessa rota.

        Endpoint: /modificar/<int:id>
        Identificador: id
    """
    ts = TeleconSchema()

    query = Telecon.query.filter(Telecon.id == id)
    query.update(request.json)
    current_app.db.session.commit()

    return ts.jsonify(query.first())


@bp_telecon.route('/inserir', methods=['POST'])
def inserir():
    """
        Função que gerencia a inserção de dados
        na tabela e retorna o registro inserido.

        O metodo POST é utilizado nessa rota.

        Endpoint: /inserir
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
