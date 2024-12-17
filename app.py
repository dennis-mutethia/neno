import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for

load_dotenv()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # One year in seconds

# Routes
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home(): 
    return render_template('home.html', page='home')

@app.route('/events', methods=['GET'])
def events(): 
    return render_template('events.html', page='events')

@app.route('/live', methods=['GET'])
def live(): 
    return render_template('live.html', page='live')

@app.route('/top-videos', methods=['GET'])
def top_videos(): 
    return render_template('videos/top.html', page='top_videos')

@app.route('/sermons', methods=['GET'])
def sermons(): 
    return render_template('videos/sermons.html', page='sermons')

@app.route('/testimonies', methods=['GET'])
def testimonies(): 
    return render_template('videos/testimonies.html', page='testimonies')

@app.route('/praise-and-worship', methods=['GET'])
def praise_and_worship(): 
    return render_template('videos/top.html', page='praise_and_worship')

@app.route('/outreach', methods=['GET'])
def outreach(): 
    return render_template('videos/outreach.html', page='outreach')

if __name__ == '__main__':
    debug_mode = os.getenv('IS_DEBUG', 'False') in ['True', '1', 't']
    app.run(debug=debug_mode)