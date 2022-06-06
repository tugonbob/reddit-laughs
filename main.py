import os
import random
import shutil
import redditApi
from moviepy.editor import *

shutil.rmtree('./ScrapedVids/', ignore_errors=True)

def create_vid():
    # get path of all vids
    vids = []
    for filename in os.listdir('./ScrapedVids'):
        if filename.endswith(".mp4"):
            clip = VideoFileClip(f'./ScrapedVids/{filename}')
            clip = clip.resize(height=720)
            vids.append(clip)
    random.shuffle(vids)

    redditVids = concatenate_videoclips(vids, method='chain').set_pos("center")

    background = (ImageClip("./Assets/MemeMachine.png")
        .set_duration(redditVids.duration)
        .resize((1280, 720)))

    likeAndSubscribe = (VideoFileClip('./Assets/youtubeButtons_animation.mp4')
        .set_pos(("center", "bottom")))
    likeAndSubscribe = likeAndSubscribe.fx(vfx.mask_color, color=[0, 255, 1], thr=100, s=5)

    final = CompositeVideoClip([background, redditVids, likeAndSubscribe], size=(1280, 720))

    final.write_videofile('final.mp4', threads=8, fps=24)

    
def scrape_reddit():
    reddit = redditApi.Reddit()     # init custom reddit api
    posts = reddit.get_top_vid_posts("funnyvideos", "week", max_vid_length=61, desired_duration=600)
    reddit.download_vids(posts)

if __name__ == '__main__':
    shutil.rmtree('./ScrapedVids/', ignore_errors=True)
    scrape_reddit()
    create_vid()