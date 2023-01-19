from flask import Flask
app = Flask(__name__)

version = '1.0'

@app.route('/')
def hello_world():
    return f'<h1>Hello, World ! - Pyflask Demo</h1><p>I am version <b>{version}</b>'

@app.route('/version')
def get_version():
    return '<h1>App version : <b>2.0</b></h1>'

@app.route('/test')
def get_test():
    return '<h1>You are accessing /test endpoint</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
