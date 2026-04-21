from flask import Flask

from Resources.Tests import test_bp

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


app.register_blueprint(test_bp)

if __name__ == '__main__':
    app.run(debug=True)