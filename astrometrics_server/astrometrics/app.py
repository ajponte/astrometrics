import logging
from datetime import datetime as dt
from flask import Flask, request

from config import Config as flask_config
from controllers.image import image_bp
from controllers.health import health_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(flask_config)
    _register_blueprints(app, [health_bp, image_bp])

    # For request logging
    @app.after_request
    def after_request(response):
        """
        Application logging.

        :param response: Application response.
        :return: response
        """
        logger = logging.getLogger("app.access")
        logger.info(
            "%s [%s] %s %s %s %s %s %s %s",
            request.remote_addr,
            dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
            request.method,
            request.path,
            request.scheme,
            response.status,
            response.content_length,
            request.referrer,
            request.user_agent,
        )
        return response

    return app


def _register_blueprints(flask_app, blueprints: list) -> None:
    for blueprint in blueprints:
        flask_app.register_blueprint(blueprint)

    return None
