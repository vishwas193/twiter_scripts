import tweepy
import time,json
import matplotlib.pyplot as plt
import numpy as np

consumer_key='<consumer_key>'
consumer_secret='<consumer_secret>'

access_key='<access_key>'
access_secret='<access_secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

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
plt.xticks(x_axis_coordinates_1,friend_name, fontsize=10, rotation=90)
plt.show()


##############################################################################


##############################################################################
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
