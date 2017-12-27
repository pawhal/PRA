from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://paw:1234@77.55.217.112/paw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7d441f27d441f27567dasfagsfrgty3546t3y46fyd63'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

from models import *


@app.route("/")
def home_site():
    return render_template("index.html")

@app.route("/questions")
def questions_site():
    return render_template("questions.html")

@app.route("/success")
def success_site():
    return render_template("success.html")

@app.route("/register", methods=['GET','POST'])
def resgister_site():
    form = Register(request.form)
    u1 = User()
    if request.method == 'POST':
        name = request.form['name']
        u1.name = name
        password = request.form['password']
        u1.password = password
        email = request.form['email']
        u1.email = email
        if form.validate():
            flash('Thanks for registration ' + name)
            db.session.add(u1)
            db.session.commit()
        else:
            flash('All fields required')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
    if form.validate():
        if User.query.filter_by(name = name) != None: #nie działa
            return render_template('success.html')
        login()
        flash('Logged in successfully.')

        return render_template('add.html')
    return render_template('login.html', form=form)


@app.route("/add", methods=['GET', 'POST'])
@login_required
def add_site():
    form = AddQ(request.form)
    q1 = Question()
    if request.method == 'POST':
        question = request.form['question']
        q1.question = question
        a = request.form['a']
        q1.a = a
        b = request.form['b']
        q1.b = b
        c = request.form['c']
        q1.c = c
        d = request.form['d']
        q1.d = d
        ra = request.form['rightAnswer']
        q1.rightAnswer = ra

        if form.validate():
            flash('valid')
            db.session.add(q1)
            db.session.commit()
        else:
            flash('invalid')

    return render_template('add.html', form=form)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")