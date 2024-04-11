from flask import Flask,jsonify
from eventlet import wsgi
import eventlet


def create_app():
    app = Flask(__name__)

    @app.route("/",methods = ["GET"])
    def get_route():
        return jsonify(status = "success", message= "Hello")

    return app


if __name__ == "__main__":
    app = create_app()

    # app.run(host="0.0.0.0",port = "5173",debug = True)
    wsgi.server(eventlet.listen(("0.0.0.0", 2003)), app, debug=False)