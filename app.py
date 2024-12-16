import os
from dotenv import load_dotenv
from flask import Flask, redirect, url_for

from utils.home import Home

load_dotenv()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # One year in seconds

# Routes
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home(): 
    return Home()() 

if __name__ == '__main__':
    debug_mode = os.getenv('IS_DEBUG', 'False') in ['True', '1', 't']
    app.run(debug=debug_mode)