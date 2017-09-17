from flask import Flask
from config import config
from flask_socketio import SocketIO

socketio = SocketIO()


def initialize(configuration):
    app = Flask(__name__)
    app.config.from_object(config[configuration])
    config[configuration].init_app(app)
    socketio.init_app(app)

    from ctps.analytics import analytics as analytics_blueprint

    app.register_blueprint(analytics_blueprint)

    return app
