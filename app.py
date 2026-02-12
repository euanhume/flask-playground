from __future__ import annotations

from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def hello() -> str:
        return "Hello, Flask!"

    @app.get("/healthz")
    def healthz():
        return jsonify(status="ok")

    return app


app = create_app()


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=5000, debug=True)
