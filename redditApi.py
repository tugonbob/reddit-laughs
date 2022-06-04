import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id='z-5lJ-uWbatBGHSKW3NqiQ', client_secret='lhQnk7SNnS2EdlQz8bXnQe8uCqw6Eg', user_agent='YtLaughs')

hot_posts = reddit.subreddit('AskReddit').hot(limit=1)

for posts in hot_posts:
    print(posts.title)
    submission = reddit.submission(id=posts.id)
    for comment in submission.comments:
        if isinstance(comment, MoreComments):
            continue
        print(comment.body)