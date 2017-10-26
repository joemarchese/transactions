from wtforms import Form, StringField, DateField, DecimalField, IntegerField, validators


class AddTransactionForm(Form):
    date = DateField('Date', [validators.DataRequired()])
    kind = StringField('Kind', [validators.DataRequired()])
    category = StringField('Category', [validators.DataRequired()])
    sub_category = StringField('Sub-Category', [validators.DataRequired()])
    description = StringField('Description', [validators.Optional()])
    amount = DecimalField('Amount', [validators.DataRequired()])

class DeleteTransactionForm(Form):
    transaction_id = IntegerField('Transaction ID', [validators.DataRequired()])
