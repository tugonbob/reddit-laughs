import redditApi
from pick import pick

reddit = redditApi.Reddit()

posts = reddit.get_top_posts("AskReddit", 'week')

title = "Top Posts"
options = [post.title for post in posts]

option, index = pick(options, title, indicator='=>')
print(option, index)