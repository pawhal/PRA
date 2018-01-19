from flask import Flask, request, render_template, redirect, session, jsonify
import requests
import json

server = 'http://127.0.0.2:5000'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjdgfsf78gyb5i4u8bgw876gb9osfvg8659oa86rvg9o'


@app.route('/', methods=['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        if session.get('user'):
            return redirect("/myreceipts")

        else:
            return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    username = request.form["username"]
    password = request.form["password"]

    credentials = {
        "username": username,
        "password": password
    }
    r = json.dumps(credentials)
    req = requests.post(server + '/register', json=r)
    if req.status_code == 583:
        return redirect("/")
    return redirect("/register")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    credentials = {
        "username": username,
        "password": password
    }
    r = json.dumps(credentials)
    req = requests.post(server + '/login', json=r)
    if req.status_code == 583:
        session['user'] = username
    return redirect("/")


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect("/")


@app.route('/addreceipt', methods=['GET', 'POST'])
def addreceipt():
    if request.method == 'GET':
        return render_template("addreceipt.html")
    if request.method == 'POST':
        user = session['user']
        name = request.form["name"]
        category = request.form["category"]
        cost = request.form["cost"]
        datetime = request.form["date"]

        receipt = {
            "user": user,
            "name": name,
            "category": category,
            "cost": cost,
            "datetime": datetime
        }
        r = json.dumps(receipt)
        req = requests.post(server + '/addreceipt', json=r)
        if req.status_code == 583:
            return redirect("/")
        else:
            return redirect("/addreceipt")


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        return render_template("edit.html")
    if request.method == 'POST':
        user = session['user']
        name = request.form["name"]
        category = request.form["category"]
        cost = request.form["cost"]
        datetime = request.form["date"]

        receipt = {
            "user": user,
            "name": name,
            "category": category,
            "cost": cost,
            "datetime": datetime
        }
        r = json.dumps(receipt)
        req = requests.post(server + '/addreceipt', json=r)
        if req.status_code == 583:
            return redirect("/myreceipts")
        else:
            return redirect("/edit")



@app.route('/myreceipts', methods=['GET', 'POST'])
def myreceipts():
    user = session['user']
    mr = {"user": user}
    r = json.dumps(mr)
    r = requests.post(server + '/myreceipts', json=r)

    response = json.loads(r.content)
    response = response['receipts']


    return render_template("myreceipts.html", **locals())


if __name__ == "__main__":
    app.run(host = "localhost")