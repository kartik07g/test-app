from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

from flask_jwt_extended import JWTManager
from Resources.Tests import test_bp
from Resources.Users import user_bp
from Resources.Auth import auth_bp

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")

JWTManager(app)

app.register_blueprint(test_bp)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)