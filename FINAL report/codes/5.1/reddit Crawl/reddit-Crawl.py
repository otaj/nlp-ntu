## Using this to crawl reddits' comments and replies
## NLP crawl v1
## Writes the comments to corpus.txt
## Use notepad++ for word count (tokens)

import praw

################### Functions ###############################

# going into comments section
def checkComments(comments):
  for comment in comments:
    file.write(comment.body)
    print (comment.body)
    checkComments(comment.replies)
  

# going into sub reddits
def processSub(sub):
  sub.replace_more_comments(limit=None, threshold=0)
  checkComments(sub.comments)

################### Functions ###############################


################### Main body ###############################
# estalish connection
r = praw.Reddit(user_agent='crawling by (/u/jonangle)')


# open subreddit
mysubreddit = r.get_subreddit('The_Donald') #change here for different subreddit
subs = mysubreddit.get_hot(limit=10000) # can edit this to increase number of articles

# open file
file = open("corpus.txt","w")
for sub in subs:
  processSub(sub)

# close file
file.close()
  
################### Main body ###############################
