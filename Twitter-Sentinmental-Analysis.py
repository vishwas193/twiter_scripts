import tweepy
import time,json
import matplotlib.pyplot as plt
import numpy as np
import re
from textblob import TextBlob

consumer_key='mbhomNkOsQrfcLy4hj1joc5hY'
consumer_secret='vgJWTbbaule8QUc3UE2E1eCIUbVJuOVc8pdGbBPTxbCdz7SG3X'

access_key='2366942240-YaFJvQW17fVwZf9bv7gw0pwavqZ8nmPWSHit58I'
access_secret='BxlhTMmDsvirOmWZ2yLyhcXT1P4NyEJsp3AzTBVUc6Lny'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

print("Program started- Auth Finished")


####################################################################
retweet_count=[]
for user_tweets in tweepy.Cursor(api.home_timeline).items(50):
    retweet_count.append(user_tweets.retweet_count)
print('retweet_count-->',retweet_count)
x_axis_coordinates = np.arange(len(retweet_count))
plt.bar(x_axis_coordinates,retweet_count)
plt.xlabel('Tweets', fontsize=10)
plt.ylabel('Re-Tweet Count', fontsize=10)
plt.show()
######################################################################


#######################################################################


friend_name,count=[],[]
friends_names=["vish193","pruthvi_kul","Arup2661"]
for friend in friends_names:
    ids = []
    for page in tweepy.Cursor(api.friends_ids, screen_name=friend).pages():
        if len(ids)<100:
            ids.extend(page)
            print("No of Friends-->",len(ids))
            friend_name.append(friend)
            count.append(len(ids))
            screen_name_list = [user.screen_name for user in api.lookup_users(user_ids=ids)]
            
            #print(friends_json_all)
x_axis_coordinates_1 = np.arange(len(friend_name))
plt.bar(x_axis_coordinates_1,count)
plt.xlabel('User', fontsize=10)
plt.ylabel('Number of friends', fontsize=10)
plt.xticks(x_axis_coordinates_1,friend_name, fontsize=10, rotation=45)
plt.show()


##############################################################################


####################Sentimental Analysis of tweets######################
def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 

def tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet)) 
    if analysis.sentiment.polarity>0:
        return 'positive'
    elif analysis.sentiment.polarity==0:
        return 'neutral'
    else:
        return 'negative'


topic=input("Please enter a Topic name:")
tweets = api.search(topic, count = 200) 
user_names=[]
parsed_tweet={}
tweet_json=[]
for tweeeeeet in tweets:
    parsed_tweet['text']=tweeeeeet.text
    parsed_tweet['sentiment']=tweet_sentiment(tweeeeeet.text)
    tweet_json.append(parsed_tweet)

    json_str = json.dumps(tweeeeeet._json)
    json_str = json.loads(json_str)
    for js in json_str:
        if js=='user':
            user_names.append(json_str[js]['name'])
#print('List of Usernames tweeted about the Topic-->',user_names)

positivetweets = [tweet for tweet in tweet_json if tweet['sentiment'] == 'positive'] 
negativetweets = [tweet for tweet in tweet_json if tweet['sentiment'] == 'negative'] 
neutraltweets = [tweet for tweet in tweet_json if tweet['sentiment'] == 'neutral'] 
totalTweets=len(positivetweets)+len(negativetweets)+len(neutraltweets)
print("Count of Positive tweets",len(positivetweets),"Out of Total Tweets ",totalTweets)
print("Count of negative tweets",len(negativetweets),"Out of Total Tweets ",totalTweets)
print("Count of Neutral tweets",len(neutraltweets),"Out of Total Tweets ",totalTweets)





########################################################################



