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

# Show cleaned text 
df 


# Create function to get subjectivity 
def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity 

# Create function to get polarity
def get_polarity(text):
    return TextBlob(text).sentiment.get_polarity

# Create two new columns 
df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
df['Polarity'] = df['Tweets'].apply(get_polarity)

df 

# Plot The Word Cloud
all_words = ''.join([twts for twts in df['Tweets']])
word_cloud = WordCloud(width = 500, height = 300, random_state = 21, max_font_size = 110).generate(all_words)

plt.imshow(word_cloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()


# Create function to compute the negative, neutral and positive analysis
def get_analysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

df['Analysis'] = df['Polarity'].apply(get_analysis)
df


# Print all positive tweets 
j = 1
sorted_df = df.sorted_values(by = ['Polarity'])

for i in range(0, sorted_df.shape[0]):
    if (sorted_df['Analysis'][i] == 'Positive'): 
        print(str(j), + ') ', sorted_df['Tweets'][i])
        print()
        j = j+1

# Print all negative tweets 
j = 1
sorted_df = df.sorted_values(by = ['Polarity'], ascending = 'False')

for i in range(0, sorted_df.shape[0]):
    if (sorted_df['Analysis'][i] == 'Negative'): 
        print(str(j), + ') ', sorted_df['Tweets'][i])
        print()
        j = j+1


# Plot polarity and subjectivity
plt.figure(figsize = (8,6))
for i in rnage(0, df.shape[0]):
    plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color = 'Blue')

plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')


# Get percentage of positive tweets 
pos_tweets = df[df.Analysis == 'Positive']
pos_tweets = pos_tweets['Tweets']

round((pos_tweets.shape[0] / df.shape[0]) * 100, 1)


# Get percentage of negative tweets
neg_tweets = df[df.Analysis == 'Negative']
neg_tweets = neg_tweets['Tweets']

round((neg_tweets.shape[0] / df.shape[0]) * 100, 1)


# Show value counts 
df['Analysis'].value_counts()

# Plot and visualize counts 
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind = 'bar')
plt.show()