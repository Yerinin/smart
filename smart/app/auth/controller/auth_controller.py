from flask import request, session, g, make_response, render_template
from flask_restx import Namespace, Resource
from functools import wraps
from smart.app.auth.service.auth_service import (
    register_user,
    login_user,
    get_user_by_id,
)
from smart.utils.errors import ApiException


api = Namespace("auth", description="main related operations")

def load_logged_in_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")
        g.user = get_user_by_id(user_id) if user_id else None
        return func(*args, **kwargs)

    return wrapper


@api.route("login")
class AuthLogin(Resource):
    @api.doc("show login page")
    def get(self):
        return make_response(render_template("/auth/login.html"))
    
    @api.doc("login post")
    def post(self):
        try:
            json_data = request.get_json()
            print(json_data)
            
            user_id = login_user(json_data["username"], json_data["password"])

            # 기존에 있던 값 삭제 후 등록
            session.pop("user_id", None)
            session["user_id"] = user_id

        except ApiException as e:
            return {"password": e.message}, 400

        return user_id


@api.route("signup")
class AuthRegist(Resource):
    @api.doc("show Register Page")
    def get(self):
        return make_response(render_template("/auth/signup.html"))
    
    @api.doc("Regist Post")
    def post(self):
        try:
            json_data = request.get_json()
            
            user = register_user(
                id=json_data["id"], 
                password=json_data["password"], 
                phone=json_data["phone"]
            )
        
        except ApiException as e:
            return {"password": e.message}, 400

        return "success"

