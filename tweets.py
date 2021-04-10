print()
print()

import tweepy

# Researcher Twitter API
auth = tweepy.OAuthHandler('XV3xaBXC18JevDGCuBJUNHaT5', '0GBbyvmdQfQQpqOGdyXeTxM7cUXYZwktVQdsauPcNlK9EhlxL9')
auth.set_access_token('1071749235677237250-TerVqgDZQ9AFLVtJUOD7S5c5ExaSOL', 'CqNmOQOJmtOdhftaA4V8BAZI4NHeTQMCGreVUUQkLLd9y')
api = tweepy.API(auth)

userID = "POTUS"

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
