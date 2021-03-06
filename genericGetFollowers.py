import tweepy  #pip install tweepy
import csv
import time
import random

#account's credentials : available on twitter dashboard, when you select the app and go to keys and tokens
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

acc_screen_name = "@GUNdotIO"   #the user screen name for which the followers must be fetched
fields = ['Username']
filename = acc_screen_name+"Followers.csv"
with open(filename, 'w') as csvfile:         #this creates a csv in which all follower usernames are populated per row
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)

def OAuth():
 try:
  auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
  auth.set_access_token(access_token,access_token_secret)
  return auth
 except Exception as e:
  print("error")

def GetFollowers(acc_screen_name):
 follower_count=api.get_user(acc_screen_name).followers_count  #get total follower count
 count=1
 limit=random. randint(250,300)
 for follower in tweepy.Cursor(api.followers, acc_screen_name).items(follower_count):
  if count==limit:
   sl=random. randint(900,1800)
   print("about to sleep for"+str(sl)+"seconds")
   time.sleep(sl)					#every increment of 250-300, sleep for any number between 900 to 1800 seconds
   limit+=random. randint(250,300)
  data=[]
  print(count)
  data.append('@'+follower.screen_name)               #populate csv per row
  with open(filename, 'a') as csvfile:
   csvwriter = csv.writer(csvfile)
   csvwriter.writerow(data)
  print("updated row")
  count+=1


oAuth = OAuth()
api = tweepy.API(oAuth,wait_on_rate_limit = True)
GetFollowers(acc_screen_name)
