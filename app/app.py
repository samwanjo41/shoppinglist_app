from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK MODIFICATIONS']= False

db = SQLAlchemy(app)

class shopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,(20) primary_key=True)
    lists = db.Column(db.String(1000), primary_key=True)

def __init__(self, title, lists):
   self.title = title
   self.list = lists
   

@app.route('/')
def index():
   return render_template('create.html')

@app.route('/sign')
def sign():
   return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
  
    title = request.form['title']
    list = request.form['list']

    signature = shopping(title=title, list=list)
    db.session.add(signature)
    db.session.commit
    flash('You were just logged in!')
    return redirect(url_for('home'))
    return render_template('login.html', title=title, list=list)

@app.route('/home')
def home():
     return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
   app.run(debug = True)
