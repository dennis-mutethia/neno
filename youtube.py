from flask import Flask, render_template
from googleapiclient.discovery import build

app = Flask(__name__)

# Initialize the YouTube API client with your API key
YOUTUBE_API_KEY = 'AIzaSyA9D3TXN7i1plmgOYKUmhQHqGOKMZAH8qE'  # Replace with your actual API key
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Initialize the YouTube API client
def youtube_client():
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)

def get_channel_id_by_handle(handle):
    youtube = youtube_client()

    try:
        # Search for the channel based on the handle
        request = youtube.search().list(
            part="snippet",
            q=handle,  # Searching using the handle or channel name
            type="channel",  # Specify that we want to search for channels
            maxResults=1  # Limit to 1 result
        )
        response = request.execute()

        # Debugging: Print the response to check if 'items' is present
        print("API Response:", response)

        # Check if 'items' is in the response
        if 'items' in response and len(response['items']) > 0:
            channel_id = response['items'][0]['snippet']['channelId']
            return channel_id
        else:
            print(f"No channel found for handle: {handle}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
# Fetch the channel's videos
def get_channel_videos(channel_id, max_results=50):
    youtube = youtube_client()
    
    # Fetch the latest videos from the channel
    video_response = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        order='date',  # Order by the latest videos
        maxResults=max_results
    ).execute()

    videos = []
    for item in video_response['items']:
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        thumbnail = item['snippet']['thumbnails']['high']['url']
        videos.append({'title': title, 'video_id': video_id, 'thumbnail': thumbnail})
    
    return videos

# Fetch the live stream (if any) from the channel
def get_live_video(channel_id):
    youtube = youtube_client()
    
    # Search for live stream videos for the channel
    search_response = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        eventType='live',  # Only get live events
        type='video'  # Only videos (not playlists)
    ).execute()

    if search_response['items']:
        live_video = search_response['items'][0]
        live_video_id = live_video['id']['videoId']
        live_video_title = live_video['snippet']['title']
        return {'title': live_video_title, 'video_id': live_video_id}
    
    return None

@app.route('/')
def index():    
    # Example usage
    channel_handle  = 'SASATVGOSPEL'  # Replace with the channel's username
    channel_id = get_channel_id_by_handle(channel_handle)
    if channel_id:
        print(f"Channel ID: {channel_id}")
    else:
        print("Channel not found")
    #channel_id = 'SASATVGOSPEL'  # Replace with your channel's ID
    latest_videos = get_channel_videos(channel_id)
    live_video = get_live_video(channel_id)

    return render_template('index.html', latest_videos=latest_videos, live_video=live_video)

if __name__ == '__main__':
    app.run(debug=True)
