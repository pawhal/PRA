from manage import db
from wtforms import Form, TextField, TextAreaField, validators, PasswordField, StringField, SubmitField


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    a = db.Column(db.String(100))
    b = db.Column(db.String(100))
    c = db.Column(db.String(100))
    d = db.Column(db.String(100))
    rightAnswer = db.Column(db.CHAR)

    def __repr__(self):
        return '<Question:{1} {2}>'.format(self.question, self.rightAnswer)


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    question = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    answer = db.Column(db.CHAR)


class User(db.Model):
    def __init__(self):
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False
        self.role = "User"

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35))
    email = db.Column(db.String(35))
    password = db.Column(db.String(35))
    role = db.Column(db.String(10))
    is_authenticated = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean)
    is_anonymous = db.Column(db.Boolean)

    def get_id(self):
            return str(self.id)

    def __repr__(self):
        return '<User:{1} {2}>'.format(self.name)

# noinspection PyDeprecation,PyDeprecation,PyDeprecation,PyDeprecation,PyDeprecation,PyDeprecation
class AddQ(Form):
    question = TextField('Question:', validators=[validators.required()])
    a = TextField('a:', validators=[validators.required()])
    b = TextField('b:', validators=[validators.required()])
    c = TextField('c:', validators=[validators.required()])
    d = TextField('d:', validators=[validators.required()])
    rightAnswer = TextField('Which one is right?:', validators=[validators.required()])


class Register(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = PasswordField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])


class Login(Form):
    name = TextField('Name:', validators=[validators.required()])
    password = PasswordField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
