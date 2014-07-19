import praw
import time

r=praw.Reddit(user_agent='Dynamic gif Slideshow by /u/xiggy')
subreddit = r.get_subreddit('gifs')

imglinks = []
used = []

def lst_of_links(word, n):
	submissions = subreddit.search(word)
	for submission in submissions:
		if submission.id not in used:
			if submission.domain == 'i.imgur.com':
				imglinks.append(submission.url)
				used.append(submission.id)
	return imglinks			