from flask_wtf import FlaskForm
from wtforms import  StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired
class StudentForm(FlaskForm):
    rollno = StringField('Roll No', validators=[DataRequired()])
    name  = StringField('Name', validators=[DataRequired()])
    feesamount = FloatField('Fees Amount', validators=[DataRequired()])
    paymentmode = SelectField('Payment Mode', choices=[('Cash','Cash'),('Card','Card')],validators=[DataRequired()])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search = StringField('Search by Roll No or Name',validators=[DataRequired()])
    submit = SubmitField('Search')