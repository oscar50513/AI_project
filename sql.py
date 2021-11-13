from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# 連結資料庫
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://admin:123456@127.0.0.1:5433/testbd'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "資料庫連線成功!"

@app.route('/setup')
def setup():
    SQL = """
    CREATE TABLE students(
    sid serial NOT NULL,
    name character varying(50) NOT NULL,
    tel character varying(50),
    addr character varying(200),
    email character varying(100),
    PRIMARY KEY(sid))
    """
    db.engine.execute(SQL)
    return "資料表建立成功!"