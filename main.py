import redditApi
from pick import pick

reddit = redditApi.Reddit()

posts = reddit.get_top_posts("AskReddit", 'week')
print(posts[0].title)