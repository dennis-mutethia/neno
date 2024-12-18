import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for

from utils.youtube import Youtube

load_dotenv()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # One year in seconds

youtube = Youtube()

# Routes
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home(): 
    latest_videos = youtube.get_channel_videos(5)
    return render_template('home.html', page='home', latest_videos=latest_videos)

@app.route('/events', methods=['GET'])
def events(): 
    return render_template('events.html', page='events')

@app.route('/live', methods=['GET'])
def live(): 
    latest_videos = youtube.get_channel_videos(5)
    live_video = youtube.get_live_video()
    return render_template('live.html', page='live', latest_videos=latest_videos, live_video=live_video)

@app.route('/top-videos', methods=['GET'])
def top_videos(): 
    latest_videos = youtube.get_channel_videos()
    return render_template('videos/top.html', page='top_videos', latest_videos=latest_videos)

@app.route('/sermons', methods=['GET'])
def sermons(): 
    latest_videos = youtube.get_channel_videos()
    return render_template('videos/sermons.html', page='sermons', latest_videos=latest_videos)

@app.route('/testimonies', methods=['GET'])
def testimonies(): 
    latest_videos = youtube.get_channel_videos()
    return render_template('videos/testimonies.html', page='testimonies', latest_videos=latest_videos)

@app.route('/praise-and-worship', methods=['GET'])
def praise_and_worship(): 
    latest_videos = youtube.get_channel_videos()
    return render_template('videos/top.html', page='praise_and_worship', latest_videos=latest_videos)

@app.route('/outreach', methods=['GET'])
def outreach(): 
    latest_videos = youtube.get_channel_videos()
    return render_template('videos/outreach.html', page='outreach', latest_videos=latest_videos)

if __name__ == '__main__':
    debug_mode = os.getenv('IS_DEBUG', 'False') in ['True', '1', 't']
    app.run(debug=debug_mode)