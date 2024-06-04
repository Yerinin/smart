from flask import redirect, url_for, make_response, render_template
from flask_restx import Namespace, Resource


api = Namespace("main", description="main related operations")


@api.route("/")
@api.route("/index")
class Index(Resource):
    @api.doc("show main page")
    def get(self):
        return make_response(render_template("index.html"))
