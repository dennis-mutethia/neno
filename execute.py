
from utils.db import Db
from utils.youtube import Youtube


class Execute():
    def __init__(self):
        self.youtube = Youtube()
        self.db = Db()
    
    def __call__(self):
        for video in self.youtube.get_channel_videos(max_results=100):
            self.db.add_video(
                video['videoId'], 
                video['title'], 
                video['description'], 
                video['liveBroadcastContent'], 
                video['publishedAt']
            )
    
Execute()()
        