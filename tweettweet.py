import tweepy



auth = tweepy.OAuthHandler('Jc3WawV4aZyFSfDIdd888kCO7', 'HdDqFgf5GQ5OLBlGBUf4IGKnUcOmfpOcVC06tDddifrcmuOgwb')
auth.set_access_token('3523841473-62LC07rOJd1MMD1GfAxw73UbjdhQqps8EffMxN9', 'onPlRw87hCc0LkDI7J3T8nFLHgvsWZCmgCdLORwa4dTyl')

api = tweepy.API(auth)
user = api.me()

print(user.name)


#narcissit bot
search_string = 'python'
numbersOfTweets = 1

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
	try:
		tweet.retweet()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break



#generous bot
for follower in tweepy.Cursor(api.followers).items():
  if follower.name == 'Izanne Dalle Ave':
  	follower.unfollow()
  	break
	
		
	


