import json

from datetime import datetime

from flask import Flask, jsonify, render_template, Response
from flask_restful import Api, Resource
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)
app.config.from_object("settings.local")

prefix_html = "/"
prefix_api = r"/api/(?P<version>[-\w]+)/"


# variables javascrip para poner disponibles en el context global
@app.route(f"{prefix_html}javascript")
def get_javascript_vars() -> jsonify:
    """
    API de bienvenida
    """
    today = datetime.now()
    context = {
        "date": today.strftime("%d/%m/%Y"),
    }
    let = "let Django = " + json.dumps(context, indent=1)
    return Response(let, mimetype='application/javascript')


# Indice
@app.route(prefix_html)
def get_index() -> jsonify:
    """
    API de bienvenida
    """
    context = {
        "title": "Index",
        "sub_title": "Aplicación Flask",
    }
    return render_template("index.html", **context)


# api index
@app.route(prefix_api)
def get_index_api() -> jsonify:
    """
    API de bienvenida
    """
    return jsonify({
        "message": "Test Tecnico Crehana",
    })


# class ViewClass(Resource):

#     def get(self):

#         return jsonify({})


# api.add_resource(ViewClass, "/test/")





if __name__ == "__main__":
    app.run(debug=True, port=4000)