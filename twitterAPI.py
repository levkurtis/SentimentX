import requests
import os
import json
import pandas as pd

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
    tweets = json.dumps(json_response, indent=4, sort_keys=True)
    print(tweets)
    

    # Pandas dataframe
    # tweetsDF = pd.DataFrame(t for t in tweets)
    # tweetsDF.to_csv('testCSV.csv')


    data = tweets
    df = pd.DataFrame([x.split('},{') for x in data.split('\n')])
    print(df)


if __name__ == "__main__":
    main()