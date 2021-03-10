from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

from portfolio.models import Restaurant

class LoginForm(Form):
    email = StringField('メールアドレス：', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード', validators=[DataRequired()])
    submit = SubmitField('ログイン')

class SignupForm(Form):
    email = StringField('メールアドレス：', validators=[DataRequired(), Email('メールアドレスが誤っています')])
    restaurant = StringField('店名：', validators=[DataRequired()])
    password = PasswordField('パスワード：', validators=[DataRequired(), EqualTo('password_confirm', message='パスワードが一致していません。')])
    password_confirm = PasswordField('パスワード確認：', validators=[DataRequired()])
    submit = SubmitField('登録')

    def validate_email(self, field):
        if Restaurant.select_by_email(field.data):
            raise ValidationError('このメールアドレスは既に登録されています。')