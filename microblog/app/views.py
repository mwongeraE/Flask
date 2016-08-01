from app import app

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
