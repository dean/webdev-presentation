from flask import request, render_template
from demo import db, app
from forms import Register
from models import User

@app.route("/", methods=['GET', 'POST'])
def register():
    form = Register()
    message = ""

    if request.method == "POST":
        if form.password.data != form.confirm_pass.data:
            message="The passwords provided did not match!\n"
        elif User.query.filter_by(username=form.username.data).all():
            message="This username is taken!"
        else:
            #Add user to db
            user = User(name=form.name.data, username=form.username.data,
                password=form.password.data)
            db.session.add(user)
            db.session.commit()
            message="Registered successfully!"

    return render_template('register.html', form=form, message=message)
