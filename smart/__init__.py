from .utils import config
from flask import Flask, Blueprint
from flask_restx import Api
from smart.routes import add_namespaces
from smart.database.config import db, migrate, ma


blueprint = Blueprint("api", __name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api( #Rest api 동객체생성
        blueprint, #수집해서사용 
        title="ELICE LIBRARY WEB APPLICATION",
        description="library web service with flask restx apis",
        doc="/swagger"
    )

    add_namespaces(api)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    return app
