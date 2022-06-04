import redditApi
from pick import pick

reddit = redditApi.Reddit()

posts = reddit.get_top_posts("AskReddit", 'week')
title = "Choose an Interesting Reddit Post"
options = [post.title for post in posts]
pickedPost, pickedPostIndex = pick(options, title)

comments = reddit.get_top_comments(posts[pickedPostIndex], limit=10)
title = "Choose All Interesting Comments"
options = [comment.body for comment in comments]
chosenComments = pick(options, title, multiselect=True)

