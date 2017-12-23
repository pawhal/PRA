from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://paw:1234@77.55.217.112/paw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7d441f27d441f27567dasfagsfrgty3546t3y46fyd63'
db = SQLAlchemy(app)

@app.route("/")
def home_site():
    return render_template("index.html")

@app.route("/questions")
def questions_site():
    return render_template("questions.html")

@app.route("/success")
def success_site():
    return render_template("success.html")

@app.route("/add", methods=['GET', 'POST'])
def add_site():
    form = AddQ(request.form)
    q1 = Question()
    #print(form.errors)
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