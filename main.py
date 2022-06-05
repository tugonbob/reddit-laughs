import os
import shutil
import redditApi
from redvid import Downloader
from moviepy.editor import *

reddit = redditApi.Reddit()
redvid = Downloader(max_q=True)
redvid.path = './DownloadedRedditVids/'

shutil.rmtree('./DownloadedRedditVids/', ignore_errors=True)

def create_vid():
    # get path of all vids
    vids = []
    for filename in os.listdir('./DownloadedRedditVids'):
        if filename.endswith(".mp4"):
            clip = VideoFileClip(f'./DownloadedRedditVids/{filename}')
            # clip = clip.resize(width=1920)
            clip = clip.resize(height=1080)
            vids.append(clip)

    final = concatenate_videoclips(vids, method='compose').set_pos("center")

    logo = (ImageClip("./Assets/logo.png", )
        .set_duration(final.duration)
        .set_pos(("right", "top")))

    youtubeButtons = (ImageClip("./Assets/youtubeButtons.png")
        .set_duration(final.duration)
        .resize(0.3)
        .set_pos(("left", "top")))

    final = CompositeVideoClip([youtubeButtons, logo, final], size=(1920, 1080))

    final.write_videofile('final.mp4')

    

posts = reddit.get_top_vid_posts("dankvideos", 'week', max_vid_length=30, total_duration=30)
for post in posts:
    redvid.url = post.url
    redvid.download()

create_vid()