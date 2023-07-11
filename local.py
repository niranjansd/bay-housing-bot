# Imports
import auth
import requests
from requests_oauthlib import OAuth1
import llmquery
import os
import datetime
import re
import time
import csv
import io
import requests

# Credentials
api_key = auth.apiKey
api_secret = auth.apiSecret
access_token = auth.accessToken
access_token_secret = auth.accessTokenSecret

# Time
start_time = datetime.datetime(2023, 7, 11).timestamp()
current_time = int(time.time())

# Function to pick a random fact and generate its text blurb.
def timed_fact():
    # Hour index of the day
    i = int((current_time - start_time)/(1*3600))
    print(i)
    # Get the listings csv
    url = 'https://raw.githubusercontent.com/niranjansd/bay-housing-bot/master/listings.csv'
    r = requests.get(url)
    csv_data = r.content.decode('utf-8')
    csv_string = io.StringIO(csv_data)    
    reader = csv.DictReader(csv_string)
    data = [row for row in reader]
    # Pick a listing
    listing = data[i]
    # Generate the blurb
    text = llmquery.format_listing(listing)
    return text


# Format the blurb generated by GPT into a tweet.
def format_fact(fact):
    while len(fact) > 280:
        fact = re.split('\. |\! ', fact)
        weak = [i for i in fact if i.replace(',', '').replace(' ', '').isalpha()]
        if len(weak):
            fact.pop(fact.index(weak[-1]))
            fact = '. '.join(fact)
            continue
        weak = [i for i in fact if 'https' not in i and '$' not in i]
        if len(weak):
            fact.pop(fact.index(weak[-1]))
            fact = '. '.join(fact)
            continue
        print('Too long to tweet')
        return None
    print('Tweeting : ', fact)
    print(len(fact))
    return {"text": "{}".format(fact)}


# Connect to Twitter API
def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
    return url, auth


def main():
    payload = None
    while not payload:
        fact = timed_fact()
        payload = format_fact(fact)
    url, auth = connect_to_oauth(
        api_key, api_secret, access_token, access_token_secret
    )
    request = requests.post(
        auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
    )
    print(request.status_code, request.text)


if __name__ == "__main__":
    main()