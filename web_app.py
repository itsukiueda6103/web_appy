from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '出席管理システムへようこそ！'

if __name__ == '__main__':
    app.run()
