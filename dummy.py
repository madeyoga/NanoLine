from gag_core import Subreddits, Reddit
from nineapi.nineapi.client import  Client, APIException
import random

#gag_client = Client()
#gag_client.log_in('made_y', 'madeyoga123')

#posts = gag_client.get_posts(
#    group=32, count=50, 
#    type_='hot', 
#    entry_types=['photo', 'animated']
#    )
#for post in posts:
#   print(post.title + " : " + post.get_media_url() + "\n type: " + post.type)

#print(len(posts))


reddit = Reddit()
submission = reddit.get_submission(subreddit=Subreddits.FGOFANART)
print(submission.url)
if '.' in submission.url[-5:]:
    print("image url")
#print(submission.url[-5:])
