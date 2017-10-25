from datetime import date
from decimal import Decimal
from pony.orm import *
import csv


db = Database()

class Transaction(db.Entity):
    date = Required(date)
    kind = Required(str) # Expense, Income, Benefits
    category = Required(str)
    sub_category = Required(str)
    description = Optional(str)
    amount = Required(Decimal)


db.bind('sqlite', 'transactions.db', create_db=True)
db.generate_mapping(create_tables=True)

@db_session
def migrate_csv():
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

if __name__ == '__main__':
    migrate_csv()
