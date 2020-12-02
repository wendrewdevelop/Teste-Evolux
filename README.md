# Teste Backend Evolux

Repositório do teste para a vagade desenvolvedor backend, da empresa Evolux.

## Como rodar o projeto

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

## Como fazer as migrações

```sh
flask db init
flask db migrate
flask db upgrade
```

## Iniciar o container

```sh
sudo docker-compose up
```
O container irá rodar a partir do endereço: *http://0.0.0.0:5000/*

## Endpoints da API

- http://0.0.0.0:5000/mostrar -> Retorna os registros
- http://0.0.0.0:5000/inserir -> Criar novos registros
- http://0.0.0.0:5000/modificar/{int:id} -> Atualizar registros existentes
- http://0.0.0.0:5000/deletar/{int:id} -> Deletar registros existentes

## Dependencias

- Flask
- flask-sqlaclhemy
- flask-migrate
- flask-marshmallow
- marshmallow-sqlalchemy
- Docker e Docker-compose

```sh
pip install -r requirements.txt
```
