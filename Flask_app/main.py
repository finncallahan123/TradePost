from flask import Flask, render_template


app = Flask(__name__)

@app.route("/Register2")
def register():

    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     flash(f'Account created for {form.username.data}!', 'success')
    #     return redirect(url_for('login'))

    return render_template('register.html')
@app.route('/Login2')
def login():
    # form = LoginForm()
    # if form.validate_on_submit():
    #     if form.email.data=="bob@bob.com" and form.password.data=="bobby":
    #         flash('You have been logged in!', "success")
    #         return redirect(url_for('timeDisplay'))
    #     else: flash('Please check your username and password')

    return render_template('login.html')

@app.route('/Home')
def home():

    return render_template('home.html')
