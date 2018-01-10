from flask import Flask, render_template, request, jsonify, redirect, session
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
    return redirect("/")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json
        username = data['username']
        password = data['password']

        password = generate_password_hash(password)

        user = User.query.filter_by(name=username).first()

        if user:
            return redirect("/register")

        user = User(name=username, password=password)

        db.session.add(user)
        db.session.commit()

        return redirect("/")


@app.route("/receipts", methods=['GET'])
def receipts():
    r = Receipt.query.all()
    return jsonify(receipts=[i.serialize for i in r])


@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json

        username = data['username']
        password = data['password']

        user = User.query.filter_by(name=username).first()

        if user:
            password_hash = user.password

            if check_password_hash(password_hash, password):
                session['user'] = username

    return redirect("/")


@app.route("/addreceipt", methods=['POST'])
def addreceipt():
    if request.method == 'POST':
        user = session['user']
        data = request.json
        name = data['name']
        category = data['category']
        datetime = data['date']
        cost = float(data['cost'])

        new_receipt = Receipt(user=user, name=name, category=category, cost=cost, date=datetime)

        db.session.add(new_receipt)
        db.session.commit()

        return redirect("/addreceipt")


if __name__ == "__main__":
    app.run(host = "0.0.0.0")
