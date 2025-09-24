from flask import Flask
from views.search_view import search_bp
from config import Config
from middlewares.rate_limiter import  rate_limiter


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(search_bp)

    @app.before_request
    def before_request():
        is_limited, message = rate_limiter()
        if is_limited:
            return message

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
