from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print("메인페이지")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)