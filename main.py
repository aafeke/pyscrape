import requests
import sys
import json
import os
import psycopg2

# pip install requirements.txt

# Credentials
BEARER_TOKEN = os.environ.get('TWITTER_BEARER_TOKEN')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
DB_ADDR = "127.0.0.1"
DB_PORT = "5432"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

tweet_fields = ['id', 'text', 'author_id', 'created_at']
keywords = ['#twitterdev']

query_params = {
    'query': keywords,
    'tweet.fields': tweet_fields[3:],
    'max_results': '10'
}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url: str, params: dict) -> dict:
    """
    Make the API request.
    """

    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def db_insert(tweets: dict, fields: list):
    """
    Parse JSON into the database
    """

    try:
        connect = psycopg2.connect(
            database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_ADDR, port=DB_PORT
        )

    except:
        print("Connection could not be established")

    data = tweets["data"]
    cursor = connect.cursor()

    for tweet in data:
        my_data = [tweet[field] for field in fields]
        insert_query = "INSERT INTO Tweet VALUES (%s, %s, %s, %s);"
        cursor.execute(insert_query, tuple(my_data))
        connect.commit()

    cursor.close()
    connect.close()

def main(argv: list[str]):
    json_response = connect_to_endpoint(search_url, query_params)
    db_insert(json_response, tweet_fields)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)