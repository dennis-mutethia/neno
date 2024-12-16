
from flask import render_template

class Home():
    def __init__(self): 
        pass
    
    def __call__(self):
        return render_template('home.html', page='homef')