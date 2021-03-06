from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError

from app.moduls.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可为空，请输入你的密码'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    def validate_mail(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可为空，请输入你的密码'), Length(6, 32)])
