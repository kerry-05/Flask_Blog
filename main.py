from flask import Flask, render_template, url_for, flash
from froms import RegistrationForm, LoginForm
from werkzeug.utils import redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = """7931371687f57736c957239c63d49d379976faf754b73201e99648253745e32cb2986b024acb34e06bab42cc981fb2a5f4b6ba9ef41cf383adb8c6387d2b61ea4977982cd3e458267f1c173a074584cdb2609d421ba0d123191976acbcdb7679ed8b5f067af2fb81e332acc82c1fa0cdd595576bd3
cdb3a5d639ab8c96cf0933df21eae95dbcf8e4f6a17e1a62b127f933f6627f7c59dece19ea5f46b953f0ad91b91908169e33ead199ba055394980f3c17f2ff28592c006ea92cca5c64f5588e221ab113e18d2fa7a7f92a7425fde530e3aabcc9aa03391c1a92b1089c8b32bb29db97937360454433d
e25ba0482bb459faee1c0396dfdf74066f7ad45492b"""

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run( debug=True)