import requests
import os
import json
import pandas as pd
import re

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAEU9OAEAAAAAvng1wu5MRGnb6OjpFglkEgDanGc%3DFwb7Hh5tHvMCRHvDwF0SwHFuKJHc1vqTUhxa2cXhZFVGLjQUc5'

search_url = "https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

hashtags = '#capitolhill'
authorOfTweet = 'a'
startTime = '2020-04-01T00:00:00Z'
endTime = '2020-04-15T23:59:59Z'
maxResults = 10 # min 1 max 500

query_params = {'query': f'({hashtags})',
                'tweet.fields': 'author_id,created_at',
                'start_time':{startTime}, 
                'end_time':{endTime},
                'max_results':{maxResults}
                # 'expansions':'author_id'
                }


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    tweets = json.dumps(json_response, indent = 4, sort_keys = True)
    #print(tweets)

    tweets_to_df(tweets)


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


if __name__ == "__main__":
    main()
