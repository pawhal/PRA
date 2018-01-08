from flask import Flask, render_template, request, flash, jsonify, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://paw:1234@77.55.217.112/paw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7d441f27d441f27567dasfagsfrgty3546t3y46fyd63'
db = SQLAlchemy(app)
from models import *


@app.route("/")
def home_site():
    return render_template("index.html")


@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')

        flash('Do zobaczenia!')
    return redirect("/")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password = generate_password_hash(password)

        user = User.query.filter_by(name=username).first()

        if user:
            flash('Niestety, użytkownik o takiej nazwie już istnieje')
            return redirect("/register")

        user = User(name=username, password=password)

        db.session.add(user)
        db.session.commit()

        flash('Zarejestrowano! Możesz się teraz zalogować')

        return redirect("/")

    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(name=username).first()

        if user:
            password_hash = user.password

            if check_password_hash(password_hash, password):
                session['user'] = username

                flash('Zalogowano poprawnie!')
                return redirect("/")
        else:
            flash('Niepoprawna nazwa użytkownika lub hasło, spróbuj ponownie')
            return redirect("/login")

    return render_template("login.html")



@app.route("/addreceipt", methods=['GET','POST'])
def addreceipt():
    if request.method == "GET":
        return render_template("addreceipt.html")
    if request.method == 'POST':
        user = session['user']
        name = request.form['name']
        category = request.form['category']
        cost = float(request.form['cost'])
        date = request.form['date']

        new_receipt = Receipt(user=user, name=name, category=category, cost=cost, date=date)

        db.session.add(new_receipt)
        db.session.commit()

        flash("Dodano nowy wydatek!")

        return redirect("/addreceipt")
    return render_template("addreceipt.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0")