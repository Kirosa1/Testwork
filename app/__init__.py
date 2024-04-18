from flask import Flask
from app.route import rendering


app = Flask(__name__,template_folder='templates')
app.add_url_rule('/','rendering',rendering)


