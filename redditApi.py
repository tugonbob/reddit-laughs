import praw
from praw.models import MoreComments

class Reddit:
    def __init__(self):
        self.reddit = praw.Reddit(client_id='z-5lJ-uWbatBGHSKW3NqiQ', client_secret='lhQnk7SNnS2EdlQz8bXnQe8uCqw6Eg', user_agent='YtLaughs')

    def get_top_posts(self, subreddit, time_filter, limit=10):
        top_posts = self.reddit.subreddit(subreddit).top(time_filter=time_filter, limit=limit)
        return [post for post in top_posts]
    
    def get_top_comments(self, post, limit=5):
        submission = self.reddit.submission(id=post.id)
        submission.comment_limit = limit
        submission.comments.replace_more(limit=0)
        return [comment for comment in submission.comments]

    def get_comment_replies(self, comment):
        return comment.replies

        # hot_posts = self.reddit.subreddit(subreddit).hot(limit=limit)

        # for posts in hot_posts:
        #     submission = reddit.submission(id=posts.id)
        #     for comment in submission.comments:
        #         if isinstance(comment, MoreComments):
        #             continue
        #         print(comment.body)