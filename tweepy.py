import tweepy

# Researcher Twitter API
auth = tweepy.OAuthHandler('XV3xaBXC18JevDGCuBJUNHaT5', '0GBbyvmdQfQQpqOGdyXeTxM7cUXYZwktVQdsauPcNlK9EhlxL9')
auth.set_access_token('1071749235677237250-TerVqgDZQ9AFLVtJUOD7S5c5ExaSOL', 'CqNmOQOJmtOdhftaA4V8BAZI4NHeTQMCGreVUUQkLLd9y')
api = tweepy.API(auth)



"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
"""



userID = "POTUS"
"""
tweets1 = api.search(q='Capitol Hill',
                           tweet_mode = 'extended', count=5,
start_time='2021-04-04', end_time='2021-04-05',
                            full_text=True)
"""

tweets2 = api.search_full_archive(environment_name='staging', query='Capitol Hill')

"""
tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=10,
                           include_rts = False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
"""



for info in tweets2[:1]:
     print("ID: {}".format(info.id))
     print(info.text)
     print(info.created_at)
     #print(info)

     
     print("\n")
