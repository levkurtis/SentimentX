# Twitter Sentiment Analysis Using Python (https://www.youtube.com/watch?v=ujId4ipkBio)

# Import Libraries
import tweepy 
from textblob import TextBlob 
from wordcloud import WordCloud 
import pandas as pd 
import numpy as no
import re
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')

# API Access 
consumerKey = 'XV3xaBXC18JevDGCuBJUNHaT5'
consumerSecret = '0GBbyvmdQfQQpqOGdyXeTxM7cUXYZwktVQdsauPcNlK9EhlxL9'
accessToken = '1071749235677237250-TerVqgDZQ9AFLVtJUOD7S5c5ExaSOL'
accessTokenSecret = 'CqNmOQOJmtOdhftaA4V8BAZI4NHeTQMCGreVUUQkLLd9y'

# Create Authentification Object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

# Set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret)

# Create API object with auth information 
api = tweepy.api(authenticate, wait_on_limit = True)


# Extract 100 tweets from twitter user 
posts = api.user_timeline(screen_name = 'Bill Gates', count = 100, language = 'en', tweet_mode = 'extended')
 
# Print las 5 tweets from account
print('Show the 5 recent tweets: \n')
for tweet in posts[:5]:
    print(str(i) + ') ', tweet.full_text + '\n')
    i = i + 1

# Create Dataframe with tweets column 
df = pd.Dataframe([tweet.full_text for tweet in posts], columns = ['Tweets'])
df.head()


# Clean the text with function 
def cleanText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) #Removes @mentions
    text = re.sub(r'#', '', text) #Removes the '#' symbol
    text = re.sub(r'RT[\s]+', '', text) #Removes RT
    text = re.sub(r'https?:\/\/\S+', '' , text) #Removes Hyperlink

    return text 

df['Tweets'] = df['Tweets'].apply(cleanText)




