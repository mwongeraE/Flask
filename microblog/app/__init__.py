from flask import flask

app = Flask(__name__)
from app import views
#The script above simply creates the application object (of class Flask) and then imports the views modul
#import statement is at the end and not at the beginning of the script as it is always done, the reason is to avoid circular references
