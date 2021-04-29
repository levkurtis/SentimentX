import requests
import json
import pandas as pd

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAEU9OAEAAAAAvng1wu5MRGnb6OjpFglkEgDanGc%3DFwb7Hh5tHvMCRHvDwF0SwHFuKJHc1vqTUhxa2cXhZFVGLjQUc5'

search_url = "https://api.twitter.com/2/tweets/search/all"


startTime = '2020-04-01T00:00:00Z'
endTime = '2020-04-15T23:59:59Z'

query_params = {#'query':f'{keyword}',
                # 'start_time': {startTime},
                # 'end_time': {endTime}
                }
                
default_params = {'tweet.fields': 'author_id,created_at','max_results':11} # min 1 max 500
# our default parameters
query_params.update(default_params)


def search_input():
    # users input queries into search with this function
    print('Hello user, welcome to the Sentiment X program')
    key = ''

    print('Please put in the keyword')
    user_input  = str(input())
    if user_input != '':
        key += user_input

        print('Please put in the hashtag')
        user_input  = str(input())
        if user_input != '':
            key+= ' #' + user_input

        print('Please put in the author')
        user_input  = str(input())
        if user_input != '':
            key+= ' from:' + user_input
    else:
        print('User did not provide keyword: default keyword used')
        key = "capitol hill" # default
        
    query = {'query': key + ' lang:en'}
    query_params.update(query)    
    print(query_params)


'''
# This will be date function which will come in the future
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
'''
    


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request(
        "GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    search_input()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    tweets = json.dumps(json_response, indent=4, sort_keys=True)

    tweets_dict = json.loads(tweets)

    tweets_lst = list()

    for tweet in tweets_dict['data']:
        tweets_lst.append(tweet['text'])

    tweets_df = pd.DataFrame(tweets_lst)
    print(tweets_df)
    # tweets_df.to_csv('testCSV.csv')


if __name__ == "__main__":
    main()
