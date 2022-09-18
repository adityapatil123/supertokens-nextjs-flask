from flask import Flask
from flask_cors import CORS
from flask_s3 import FlaskS3
from supertokens_python import get_all_cors_headers
from supertokens_python.framework.flask import Middleware

import main.config
import main.auth
from main.routes import Api, api

s3 = FlaskS3()
jwt = None


def create_app(config_name):
    global jwt
    app = Flask(__name__, template_folder='templates', static_url_path='')
    app.config.from_object(config.config_by_name[config_name])
    app.app_context().push()
    api.init_app(app)
    Middleware(app)
    CORS(
        app=app,
        origins=[
            "http://localhost:3000"
        ],
        supports_credentials=True,
        allow_headers=["Content-Type"] + get_all_cors_headers(),
    )
    return app



