import os
import shutil
import redditApi
from redvid import Downloader
from moviepy.editor import *

reddit = redditApi.Reddit()
redvid = Downloader(max_q=True)
redvid.path = './DownloadedRedditVids/'

shutil.rmtree('./DownloadedRedditVids/', ignore_errors=True)

def concat_videos():
    # get path of all vids
    vids = []
    for filename in os.listdir('./DownloadedRedditVids'):
        if filename.endswith(".mp4"):
            clip = VideoFileClip(f'./DownloadedRedditVids/{filename}')
            clip = clip.resize(height=1080)
            vids.append(clip)

    final = concatenate_videoclips(vids, method='compose')
    final.write_videofile('final.mp4')

    

posts = reddit.get_top_vid_posts("dankvideos", 'day', max_vid_length=30, total_duration=300)
for post in posts:
    redvid.url = post.url
    redvid.download()

concat_videos()