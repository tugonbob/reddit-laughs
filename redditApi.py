import praw
from redvid import Downloader

class Reddit:
    def __init__(self):
        self.reddit = praw.Reddit(client_id='z-5lJ-uWbatBGHSKW3NqiQ', client_secret='lhQnk7SNnS2EdlQz8bXnQe8uCqw6Eg', user_agent='YtLaughs')

    def get_top_vid_posts(self, subreddit, time_filter,limit=None, desired_duration=300, max_vid_length=9999999999, min_vid_length=0, min_upvote_ratio=0.9):
        top_posts = self.reddit.subreddit(subreddit).top(time_filter=time_filter, limit=limit)
        result = []
        duration_sum = 0
        for post in top_posts:
            if post.media is None: continue
            vid_length = post.media['reddit_video']['duration']
            if vid_length > min_vid_length and vid_length < max_vid_length and post.upvote_ratio > min_upvote_ratio:
                duration_sum += vid_length
                result.append(post)
            if duration_sum > desired_duration:
                break
        return result


    def download_vids(self, posts):
        redvid = Downloader(max_q=True) # init redvid's reddit video downloader
        redvid.path = './ScrapedVids/'  # set downloaded videos dir
        for post in posts:
            redvid.url = post.url
            redvid.download()