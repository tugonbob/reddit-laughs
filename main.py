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
            clip = clip.resize(height=720)
            vids.append(clip)

    final = concatenate_videoclips(vids, method='compose').set_pos("center")

    logo = (ImageClip("./Assets/MemeMachine.png", )
        .set_duration(final.duration)
        .resize(height=200)
        .set_pos(("right", "top")))

    likeAndSubscribe = (VideoFileClip('./Assets/youtubeButtons_animation.mp4')
        .set_pos(("center", "bottom")))
    likeAndSubscribe = likeAndSubscribe.fx(vfx.mask_color, color=[0, 255, 1], thr=100, s=5)

    youtubeButtons = (ImageClip("./Assets/youtubeButtons.png")
        .set_duration(final.duration)
        .resize(height=200)
        .set_pos(("left", "top")))

    final = CompositeVideoClip([logo, youtubeButtons, final, likeAndSubscribe], size=(1280, 720))

    final.write_videofile('final.mp4', threads=4, fps=24)

    

posts = reddit.get_top_vid_posts("dankvideos", 'day', max_vid_length=30, desired_duration=600)
for post in posts:
    redvid.url = post.url
    redvid.download()

create_vid()