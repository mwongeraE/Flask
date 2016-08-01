from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Evans'} #fake user
    posts = [
    {
    'author': {'nickname': 'John'},
    'body': 'Beautiful day in Nairobi'
    },
    {
    'author': {'nickname': 'Susan'},
    'body': 'The Avengers movie was dumb'
    }
    ]
    return render_template('index.html',user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
        (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
