from wtforms import Form, StringField, DateField, DecimalField, validators


class AddTransactionForm(Form):
    date = DateField('Date', [validators.DataRequired()])
    kind = StringField('Kind', [validators.DataRequired()])
    category = StringField('Category', [validators.DataRequired()])
    sub_category = StringField('Sub-Category', [validators.DataRequired()])
    description = StringField('Optional')
    amount = DecimalField('Amount', [validators.DataRequired()])
