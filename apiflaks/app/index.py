from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'Test Api'

if __name__ == "__main__":
    app.run()