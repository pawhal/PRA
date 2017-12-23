from app import db
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    a = db.Column(db.String(100))
    b = db.Column(db.String(100))
    c = db.Column(db.String(100))
    d = db.Column(db.String(100))
    rightAnswer = db.Column(db.String(1))

    def __repr__(self):
        return '<Question:{1} {2}>'.format(self.question,
                                               self.rightAnswer)


# noinspection PyDeprecation,PyDeprecation,PyDeprecation,PyDeprecation,PyDeprecation,PyDeprecation
class AddQ(Form):
    question = TextField('Question:', validators=[validators.required()])
    a = TextField('a:', validators=[validators.required()])
    b = TextField('b:', validators=[validators.required()])
    c = TextField('c:', validators=[validators.required()])
    d = TextField('d:', validators=[validators.required()])
    rightAnswer = TextField('Which one is right?:', validators=[validators.required()])