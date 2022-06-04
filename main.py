import shutil
import redditApi
from pick import pick
from redvid import Downloader

reddit = redditApi.Reddit()
redvid = Downloader(max_q=True)
redvid.path = './DownloadedRedditVids/'

shutil.rmtree('./DownloadedRedditVids/', ignore_errors=True)

posts = reddit.get_top_vid_posts("dankvideos", 'day', max_vid_length=30, total_duration=300)
for post in posts:
    redvid.url = post.url
    redvid.download()

