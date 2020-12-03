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

## Endpoints da API em desenvolvimento

- http://0.0.0.0:5000/mostrar -> Retorna os registros
- http://0.0.0.0:5000/detail/{int:id} -> Retorna um registro especifico
- http://0.0.0.0:5000/inserir -> Criar novos registros
- http://0.0.0.0:5000/modificar/{int:id} -> Atualizar registros existentes
- http://0.0.0.0:5000/deletar/{int:id} -> Deletar registros existentes

## Endpoints da API em produção
- https://evolux.herokuapp.com/mostrar -> Retorna os registros
- https://evolux.herokuapp.com/detail/{int:id} -> Retorna um registro especifico
- https://evolux.herokuapp.com/inserir -> Criar novos registros
- https://evolux.herokuapp.com/modificar/{int:id} -> Atualizar registros existentes
- https://evolux.herokuapp.com/deletar/{int:id} -> Deletar registros existentes 

## Rodando testes

- Os testes foram feitos usando a lib pytest. 

Rode no terminal:

```sh
pytest
```

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
