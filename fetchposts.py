import json
import praw

 
def GetPosts(Subreddits,TopPosts):
	CompleteData = []
	SubredditData = []
	with open("UserData.json", "r") as read_file:
    		data = json.load(read_file)
	reddit = praw.Reddit(
						client_id = data["client_id"] ,
						client_secret = data["client_secret"] ,
						username = data["username"] ,
						password = data["password"] , 
						user_agent = data["user_agent"]
						)
	for i in range(len(Subreddits)):
		print(Subreddits[i])
		subreddit = reddit.subreddit(Subreddits[i])
		for submission in subreddit.hot(limit=TopPosts):
			if ".png" in submission.url or ".webp" in submission.url or ".jpeg" in submission.url or ".jpg" in submission.url:
				imgurl = submission.url
			else:
				imgurl = False
			SubmissionData = [submission.title,submission.selftext,submission.author.name,imgurl,submission.comments]
			SubredditData.append(SubmissionData)
		CompleteData.append(SubredditData)
	return CompleteData



