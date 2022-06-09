import os
import random
import argparse
import shutil
import redditApi
from moviepy.editor import *
import pandas as pd


def create_vid():
    if args.verbose: print("Rendering the final video")

    # get path of all vids
    vids = []
    for filename in os.listdir('./ScrapedVids'):
        if filename.endswith(".mp4"):
            clip = VideoFileClip(f'./ScrapedVids/{filename}')
            clip = clip.resize(height=720)
            vids.append(clip)
    random.shuffle(vids)

    redditVids = concatenate_videoclips(vids, method='chain').set_pos("center")

    likeAndSubscribe = (VideoFileClip('./Assets/youtubeButtons_animation.mp4')
        .set_pos(("center", "bottom")))
    likeAndSubscribe = likeAndSubscribe.fx(vfx.mask_color, color=[0, 255, 1], thr=100, s=5)

    final = CompositeVideoClip([redditVids, likeAndSubscribe], size=(1280, 720))

    final.write_videofile('final.mp4', threads=8, fps=24)

    
def scrape_reddit():
    reddit = redditApi.Reddit()     # init custom reddit api
    for index, row in df.iterrows():
        try:
            if args.verbose: print(f"Scraping {row['DesiredDuration']} seconds of videos from r/{row['Subreddit']} that is the top of the last {row['TimeFilter']}")
            posts = reddit.get_top_vid_posts(row['Subreddit'], row['TimeFilter'], desired_duration=row['DesiredDuration'])
            reddit.download_vids(posts)
        except Exception as e:
            raise Exception(e)


# main
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", default=False, action='store_true', help="Verbose mode")
args = parser.parse_args()

if args.verbose: print("Reading from 'SelectedSubreddits.csv'")
df = pd.read_csv('SelectedSubreddits.csv')

if args.verbose: print("Deleting the 'ScrapedVids' directory")
shutil.rmtree('./ScrapedVids/', ignore_errors=True)

scrape_reddit()
create_vid()