from manage import db


class User(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(35), primary_key=True, unique=True)
    password = db.Column(db.String(200))


class Category(db.Model):
    __tablename__ = 'categories'
    name = db.Column(db.String(35), primary_key=True)


class Receipt(db.Model):
    __tablename__ = 'receipts'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(35), db.ForeignKey('users.name'))
    name = db.Column(db.String(50))
    category = db.Column(db.String(25), db.ForeignKey('categories.name'))
    cost = db.Column(db.Numeric)
    date = db.Column(db.DateTime)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'category': self.category,
            'cost': float(self.cost),
            'date': self.date
        }