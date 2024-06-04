import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = "mysql://root:pi@localhost/smart"
SQLALCHEMY_TRACK_MODIFICATIONS = False #mysql commit request->transaction 
