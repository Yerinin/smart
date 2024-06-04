from datetime import datetime
from pytz import timezone
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from smart.database.config import db


class User(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)

    def __init__(self, id, password, phone):
        self.id = id
        self.password = generate_password_hash(password)
        self.phone = phone
        self.created_at = datetime.now(timezone("Asia/Seoul"))

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_password(self, password):
        self.password = generate_password_hash(password)
        return self

    def __repr__(self):
        return (
            "<User(id='%s', password='%s', phone='%s', created_at='%s')>"
            % (self.id, self.password, self.phone, self.created_at)
        )

    @staticmethod
    def create(id, password, phone):
        return User(id=id, password=password, phone=phone)