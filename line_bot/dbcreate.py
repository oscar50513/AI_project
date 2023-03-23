from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# 連結資料庫
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://oscar:123456@127.0.0.1:5433/test'
db = SQLAlchemy(app)

# 定義資料類型
class students(db.Model):
    __tablename__ = 'students'
    sid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    tel = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    email = db.Column(db.String(100))
    
    def __int__(self, name, tel, addr, email):
        self.name = name
        self.tel = tel
        self.addr = addr
        self.email = email
        
@app.route('/')
def index():
    db.create_all()# 建立定義好的資料表物件
    return "資料庫連線成功!"

@app.route('/insert')
def insert():
    student = students('炭治郎', '0911111111', '台北市信義路101號', 'tjl@test.com')
    db.session.add(student)
    db.session.commit() #提交db.session的資料到資料庫
    return "資料新增成功!"

@app.route('/insertall')
def insertall():
    datas = [students('彌豆子', '0922222222', '台北市南京東路50號', 'mdj@test.com'), 
             students('伊之助', '0933333333', '台北市北門路20號', 'yjj@test.com')]
    db.session.add(datas)
    db.session.commit() #提交db.session的資料到資料庫
    return "資料批次新增成功!"

if __name__ == '__main__':
    app.run(debug=True)