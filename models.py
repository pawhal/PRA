from manage import db


class User(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(35), primary_key=True, unique=True)
    password = db.Column(db.String(200))

    def __repr__(self):
        return '<User:{0}>'.format(self.name)


class Receipt(db.Model):
    __tablename__ = 'receipts'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(35), db.ForeignKey('users.name'))
    name = db.Column(db.String(50))
    category = db.Column(db.String(25))
    cost = db.Column(db.Numeric)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Receipt:{0} {1}>'.format(self.name, self.cost)

