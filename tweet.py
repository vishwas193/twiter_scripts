import tweepy
import time,json

consumer_key='mbhomNkOsQrfcLy4hj1joc5hY'
consumer_secret='vgJWTbbaule8QUc3UE2E1eCIUbVJuOVc8pdGbBPTxbCdz7SG3X'

access_key='2366942240-YaFJvQW17fVwZf9bv7gw0pwavqZ8nmPWSHit58I'
access_secret='BxlhTMmDsvirOmWZ2yLyhcXT1P4NyEJsp3AzTBVUc6Lny'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

retweet_count=[]
for user_tweets in tweepy.Cursor(api.home_timeline).items(50):
    #print(user_tweets.text)
    retweet_count.append(user_tweets.retweet_count)
print(retweet_count)


ids = []
for page in tweepy.Cursor(api.friends_ids, screen_name="vish193").pages():
    if len(ids)<100:
        ids.extend(page)
        print(len(ids))
screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]

topic=input("Please enter a Topic name:")

tweets = api.search(topic, count = 200) 
user_names=[]
for tweeeeeet in tweets:
    json_str = json.dumps(tweeeeeet._json)
    json_str = json.loads(json_str)
    for js in json_str:
        if js=='user':
            user_names.append(json_str[js]['name'])
print('List of Usernames tweeted about the Topic-->',user_names)
