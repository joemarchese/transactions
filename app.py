from flask import Flask, render_template, url_for
from models import db, Transaction
from datetime import date
import csv
import sys



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
db.init_app(app)

@app.route('/')
def index():
    transactions = Transaction.query.all()
    return render_template('index.html', transactions=transactions)

if __name__ == '__main__':
    if 'convert_csv' in sys.argv:
        with app.app_context():
            try: # delete the Database if it already exists.
                db.session.query(Transactions).delete()
                db.session.commit()
            except:
                pass
            db.create_all()
            with open('Income - Expenses - Transactions.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    year, month, day = [int(i) for i in row['Date'].split('/')]
                    transaction = Transaction(date=date(year, month, day),
                                              kind=row['Kind'],
                                              category=row['Category'],
                                              sub_category=row['Type'],
                                              description=row['Description'],
                                              amount=row['Amount'])
                    db.session.add(transaction)
                    db.session.commit()
    else:
        app.run(debug=True)
