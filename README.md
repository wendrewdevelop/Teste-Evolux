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

## Dependencias

- Flask
- flask-sqlaclhemy
- flask-migrate
- flask-marshmallow
- marshmallow-sqlalchemy

```sh
pip install -r requirements.txt
```

# TO-DO

- [ ] Docker;