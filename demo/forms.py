from wtforms import Form, TextField, PasswordField
from wtforms.validators import Required
from models import User

class Register(Form):
    name = TextField('name', [Required()])
    username = TextField('username', [Required()])
    password = PasswordField('password', [Required()])
    confirm_pass = PasswordField('confirm_pass', [Required()])
