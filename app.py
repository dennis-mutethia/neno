import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for, request

from utils.db import Db

load_dotenv()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # One year in seconds

db = Db()

# Routes
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():                 
    latest_videos = db.get_videos(liveBroadcastContent='none', limit=4)
    return render_template('home.html', page='home', latest_videos=latest_videos)

@app.route('/events', methods=['GET'])
def events(): 
    return render_template('events.html', page='events')

@app.route('/live', methods=['GET'])
def live(): 
    latest_videos = db.get_videos(liveBroadcastContent='none', limit=4)
    live_videos = db.get_videos(liveBroadcastContent='live', limit=1)
    return render_template('live.html', page='live', latest_videos=latest_videos, live_videos=live_videos)

@app.route('/top-videos', methods=['GET'])
def top_videos(): 
    current_page = int(request.args.get('current_page', 1))
    limit = 10
    latest_videos = db.get_videos(liveBroadcastContent='none', limit=limit, current_page=current_page)
    next_page = current_page+1 if len(latest_videos) == limit else 0
    return render_template('videos/top.html', page='top_videos', latest_videos=latest_videos, current_page=current_page, next_page=next_page)

@app.route('/sermons', methods=['GET'])
def sermons(): 
    latest_videos = db.get_videos(liveBroadcastContent='none', limit=10)
    return render_template('videos/sermons.html', page='sermons', latest_videos=latest_videos)

@app.route('/testimonies', methods=['GET'])
def testimonies(): 
    latest_videos = db.get_videos(liveBroadcastContent='none', limit=10)
    return render_template('videos/testimonies.html', page='testimonies', latest_videos=latest_videos)

@app.route('/praise-and-worship', methods=['GET'])
def praise_and_worship(): 
    latest_videos = db.get_videos(liveBroadcastContent='none', limit=10)
    return render_template('videos/top.html', page='praise_and_worship', latest_videos=latest_videos)

@app.route('/outreach', methods=['GET'])
def outreach(): 
    latest_videos = db.get_videos(liveBroadcastContent='none', limit=10)
    return render_template('videos/outreach.html', page='outreach', latest_videos=latest_videos)

if __name__ == '__main__':
    debug_mode = os.getenv('IS_DEBUG', 'False') in ['True', '1', 't']
    app.run(debug=debug_mode)