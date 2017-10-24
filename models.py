from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today())
    kind = db.Column(db.String) # Expense, Income, Benefits
    category = db.Column(db.String)
    sub_category = db.Column(db.String)
    description = db.Column(db.Text)
    amount = db.Column(db.Float(precision=2))
