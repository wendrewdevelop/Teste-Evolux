import unittest
from flask import Flask, request, jsonify
from app import create_app
from app.model import db


def test_create_app_deve_retornar_um_app_flask():
        assert isinstance(create_app(), Flask)


def test_verificando_listagem_dados_api():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        response = client.get('/mostrar')

    assert response.status_code == 200


def test_verificando_insercao_dados_api():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        response = client.post(
            '/inserir',
            json={
                'value': '+55 16 99734-0239', 
                'monthyPrice': '25.90',
                'setupPrice': '60.00',
                'currency': 'R$',
            }
        )

    assert response.status_code == 201


def test_verificando_update_dados_api():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        response = client.post(
            '/modificar/1',
            json={
                'value': '+55 16 98179-3551', 
                'monthyPrice': '33.00',
                'setupPrice': '66.06',
                'currency': 'U$',
            }
        )

    assert response.status_code == 200    


def test_verificando_delete_dados_api():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        response = client.delete('/deletar/1')

    assert response.status_code == 405       