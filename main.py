import redditApi
from pick import pick

reddit = redditApi.Reddit()

posts = reddit.get_top_posts("AskReddit", 'week')

title = "Choose an Interesting Reddit Post"
options = [post.title for post in posts]
pickedPost, pickedPostIndex = pick(options, title)

comments = reddit.get_top_comments(posts[pickedPostIndex])
title = "Choose All Interesting Comments"
options = [comment.body for comment in comments]
chosenComments = [comment[0] for comment in pick(options, title, multiselect=True, min_selection_count=1)]
print(chosenComments)