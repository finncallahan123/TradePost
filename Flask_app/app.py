from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def Home():

    return render_template('Home.html')

@app.route("/Register2")
def Register2():

    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     flash(f'Account created for {form.username.data}!', 'success')
    #     return redirect(url_for('login'))

    return render_template('Register2.html')
@app.route('/Login2')
def Login2():
    # form = LoginForm()
    # if form.validate_on_submit():
    #     if form.email.data=="bob@bob.com" and form.password.data=="bobby":
    #         flash('You have been logged in!', "success")
    #         return redirect(url_for('timeDisplay'))
    #     else: flash('Please check your username and password')

    return render_template('Login2.html')


@app.route('/Feed')
def Feed():

    return render_template('IndexTP.html')
