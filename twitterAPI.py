import requests
import json
import pandas as pd
import re

from config import bearer_token # imports bearer token from API

search_url = "https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
print('Please input keyword')
keyword = str(input())
# print('Please input author')
# author = str(input())
# print('Please hashtag')
# hashtags = '#' + str(input())


startTime = '2020-04-01T00:00:00Z'
endTime = '2020-04-15T23:59:59Z'


query_params = {'query':f'{keyword}',
                'start_time': {startTime},
                'end_time': {endTime}
                }
                
default_params = {'tweet.fields': 'author_id,created_at','max_results':10} # min 1 max 500
# our default parameters
query_params.update(default_params)



'''
def search_input(dict_search):
    dict_search = {}
    print('Hello user, welcome to the Sentiment X program')
    # keyword
    print('Please put in the keyword')
    user_input = str(input())
    if user_input != '':
        keyword = user_input
        dict_search['keyword'] = keyword
    else:
        print('keyword not inputed')

    # author
    print('Please input the author of the tweet')
    user_input = str(input())
    if user_input != '':
        authorOfTweet = user_input
        dict_search['author'] = authorOfTweet
    else:
        print('author not inputed')
        authorOfTweet = ''

    # hashtag
    print('Please input the hashtag')
    user_input = str(input())
    if user_input != '':
        hashtag = user_input
        dict_search['hashtag'] = hashtag
    else:
        print('hashtag not inputed')

    # start date
    print('Please input the start date')
    user_input = str(input())
    if user_input != '':
        startTime = user_input
        dict_search['Start Date'] = startTime
    else:
        print('date not inputed')

    # end date
    print('Please input the end date')
    user_input = str(input())
    if user_input != '':
        endTime = user_input
        dict_search['End Date'] = endTime
    else:
        print('date not inputed')

    print(dict_search)
    return dict_search
'''
    


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

# Main program
def main():
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    tweets = json.dumps(json_response, indent = 4, sort_keys = True)
    #print(tweets)

    tweets_to_df(tweets)

# Cleans and puts tweets into Pandas DataFrame
def tweets_to_df(tweets):
    tweets_dict = json.loads(tweets) # creates pythond dict from json string 

    tweets_lst = list()

    for tweet in tweets_dict['data']:
        tweets_lst.append(tweet['text']) # iterates over dict value 'data' and appends each 'text' to list
    
    tweets_df = pd.DataFrame(tweets_lst, columns = ['Text']) # turns list into dataframe and assigs column names
    
    tweets_df.insert(0, 'Index', [1, 2, 3, 4, 5, 6, 7, 8, 9], True) # create and add column with index for each row
    tweets_df = tweets_df.set_index('Index') # set 'Index' column as index
    tweets_df.info()


    def clean_text(text):
        text = re.sub(r'@[A-Za-z0-9]+', '', text) # Removes @mentions
        text = re.sub(r'#[A-Za-z0-9]+', '', text) # Removes the '#' symbol
        text = re.sub(r'RT[\s]+', '', text) # Removes RT
        text = re.sub(r'https?:\/\/\S+', '' , text) # Removes Hyperlink
        text = re.sub(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', '', text) # Removes non latin characters
        
        return text 

    tweets_df = tweets_df['Text'].apply(clean_text)

    print(tweets_df)
    # tweets_df.to_csv('testCSV.csv')


if __name__ == "__main__":
    main()
