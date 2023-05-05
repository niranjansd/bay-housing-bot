import auth
import requests
from requests_oauthlib import OAuth1
import pandas as pd
import llmquery
import os
import re
import time
import csv
import io
import requests


# consumer_key = os.environ.get("CONSUMER_KEY")
# consumer_secret = os.environ.get("CONSUMER_SECRET")
# access_token = os.environ.get("ACCESS_TOKEN")
# access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
api_key = auth.apiKey
api_secret = auth.apiSecret
access_token = auth.accessToken
access_token_secret = auth.accessTokenSecret

# print(os.getcwd())
start_time = 1683251330
current_time = int(time.time())


def random_fact():
    i = (current_time - start_time)//(1*3600)
    print(i)
    url = 'https://raw.githubusercontent.com/niranjansd/bay-housing-bot/master/listings.csv'
    r = requests.get(url)
    csv_data = r.content.decode('utf-8')
    csv_string = io.StringIO(csv_data)    
    reader = csv.DictReader(csv_string)
    data = [row for row in reader]
    listing = data[i]
    text = llmquery.format_listing(listing)
    return text


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


def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
    return url, auth


def main():
    payload = None
    while not payload:
        fact = random_fact()
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