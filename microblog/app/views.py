from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"
#The two route decorators above the function create the mappings from URLs / and /index to this function.
