import requests
import sys
import json
import os

argv = sys.argv[1:]

# Credentials
BEARER_TOKEN = os.environ.get('TWITTER_BEARER_TOKEN')
DB_PASS = os.environ.get('DB_PASS')
DB_ADDR = "127.0.0.1"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {
    'query': '#twitterdev',
    'tweet.fields': 'author_id,created_at',
    'max_results': '10'
}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url: str, params: dict):
    """
    Make the API request.
    """

    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main(argv: list[str]):
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main(argv)