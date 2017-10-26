from flask import Flask, render_template, url_for, request, redirect
from models import db, Transaction
from forms import AddTransactionForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
db.init_app(app)

@app.route('/')
def index():
    transactions = Transaction.query.all()
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddTransactionForm(request.form)
    if request.method == 'POST' and form.validate():
        with app.app_context():
            transaction = Transaction(date=form.date.data,
                                      kind=form.kind.data,
                                      category=form.category.data,
                                      sub_category=form.sub_category.data,
                                      description=form.description.data,
                                      amount=form.amount.data)
            db.session.add(transaction)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
