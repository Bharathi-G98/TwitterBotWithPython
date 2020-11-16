import tweepy  #pip install tweepy
import csv
import random
import time

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def OAuth():
 try:
  auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
  auth.set_access_token(access_token,access_token_secret)
  return auth
 except Exception as e:
  print("error")

def PostTweet(message):
 api.update_status(message)
 print("tweet has been posted")
 
def followUser(username):  #i.e."@google"
 try:
  api.create_friendship(username)
  print("user followed successfully")
 except Exception as e:
  print("error")

def UpdateFollowers(acc_screen_name):
 randMsgTweeted=[]
 usersFollowed=[]
 #follower_count=api.get_user(acc_screen_name).followers_count
 limit=20
 randMsg=8
 for i in range(185,len(codementorFollowers)):
  if i==limit:
   s=random. randint(300,900)
   #time.sleep(s)
   comp=competitors[random. randint(0,len(competitors)-1)]
   user=comp[random. randint(0,len(comp)-1)]
   if usersFollowed:
    while user in usersFollowed:
     comp=competitors[random. randint(0,len(competitors)-1)]
     user=comp[random. randint(0,len(comp)-1)]
   usersFollowed.append(user)
   followUser(user) 
   limit+=random. randint(12,20)
   time.sleep(s)
  if i==randMsg:
    mInd=random. randint(0,len(randMessages)-1)
    if randMsgTweeted:
     while mInd in randMsgTweeted:
      mInd=random. randint(0,len(randMessages)-1)
    randMsgTweeted.append(mInd)
    mes=randMessages[mInd]
    PostTweet(mes)
    sl=random. randint(300,900)
    randMsg+=random. randint(10,15)
    print("about to sleep for"+str(sl)+"seconds")
    time.sleep(sl)
  mInd=random. randint(0,len(messages)-1)
  message=messages[mInd].replace("@username",codementorFollowers[i])
  message=message.replace("crewscale.com","https://bit.ly/2TKjx9V")
  PostTweet(message)
  sl=random. randint(1800,3600)
  print("about to sleep for"+str(sl)+"seconds")
  time.sleep(sl)

competitors=[]
"""
upworkFollowers=[]
with open('/home/ubuntu/Twitter/@UpworkFollowers.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        upworkFollowers.append(row[0])
upworkFollowers=upworkFollowers[1:]
competitors.append(upworkFollowers)
"""

codementorFollowers=[]
with open('/home/ubuntu/Twitter/@CodementorIOFollowers.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        codementorFollowers.append(row[0])
codementorFollowers=codementorFollowers[1:]
#competitors.append(codementorFollowers)

gigsterFollowers=[]
with open('/home/ubuntu/Twitter/@trygigsterFollowers.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        gigsterFollowers.append(row[0])
gigsterFollowers=gigsterFollowers[1:]
competitors.append(gigsterFollowers)

xteamFollowers=[]
with open('/home/ubuntu/Twitter/@xteamFollowers.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        xteamFollowers.append(row[0])
xteamFollowers=xteamFollowers[1:]
competitors.append(xteamFollowers)

toptalFollowers=[]
with open('/home/ubuntu/Twitter/ToptalFollowers.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        toptalFollowers.append(row[0])
toptalFollowers=toptalFollowers[1:]
competitors.append(toptalFollowers)


messages=[]
with open('/home/ubuntu/Twitter/crewscaleMessagesNew.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        messages.append(row[0])
messages=messages[1:]
randMessages=[]
with open('/home/ubuntu/Twitter/remote.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        randMessages.append(row[0])
randMessages=randMessages[1:]
oAuth = OAuth()
api = tweepy.API(oAuth,wait_on_rate_limit = True)
acc_screen_name = "@CodementorIO"   #the user screen name for which the followers must be fetched
#image_path="C://Users//Lenovo//Downloads//crewscale.jpeg"
UpdateFollowers(acc_screen_name)

def OAuth():
 try:
  auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
  auth.set_access_token(access_token,access_token_secret)
  return auth
 except Exception as e:
  print("error")

def PostTweet(message):
 api.update_status(message)
 print("tweet has been posted")
 
def followUser(username):  #i.e."@google"
 try:
  api.create_friendship(username)
  print("user followed successfully")
 except Exception as e:
  print("error")

def UpdateFollowers(acc_screen_name):
 #follower_count=api.get_user(acc_screen_name).followers_count
 limit=20
 randMsg=8
 for i in range(len(followers)):
  if i==limit:  #to follow a random user of a random competitor in the competitors list
   s=random. randint(300,900)
   comp=competitors[random. randint(0,len(competitors)-1)]
   followUser(comp[random. randint(0,len(comp)-1)]) 
   limit+=random. randint(12,20)
   time.sleep(s)
  if i==randMsg: #to post a random generic tweet
    mInd=random. randint(0,len(randMessages)-1)
    mes=randMessages[mInd]
    PostTweet(mes)
    sl=random. randint(300,900)
    randMsg+=random. randint(10,15)
    print("about to sleep for"+str(sl)+"seconds")
    time.sleep(sl)
  mInd=random. randint(0,len(messages)-1)
  message=messages[mInd].replace("@username",followers[i])
  message=message.replace("crewscale.com","https://bit.ly/2TKjx9V")
  PostTweet(message)
  sl=random. randint(1800,3600)
  print("about to sleep for"+str(sl)+"seconds")
  time.sleep(sl)

competitors=[]   #this is a list of all other competetitors for which followers have been obtained
competitorsFollowers1=[]
with open('/home/ubuntu/Twitter/competitorsFollowers1.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        competitorsFollowers.append(row[0])
competitorsFollowers1=competitorsFollowers1[1:]
competitors.append(competitorsFollowers1)

competitorsFollowers2=[]
with open('/home/ubuntu/Twitter/competitorsFollowers2.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        competitorsFollowers2.append(row[0])
competitorsFollowers2=competitorsFollowers2[1:]
competitors.append(competitorsFollowers2)
# do the same for all other competitors

messages=[]  #these are the messages in which foollower usernames are added and tweeted
with open('/home/ubuntu/Twitter/crewscaleMessagesNew.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        messages.append(row[0])
messages=messages[1:]

randMessages=[]  #these are random generic messages tweeted at regular intervals
with open('/home/ubuntu/Twitter/remote.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        randMessages.append(row[0])
randMessages=randMessages[1:]
oAuth = OAuth()
api = tweepy.API(oAuth,wait_on_rate_limit = True)
acc_screen_name = "@gigster"   #the user screen name for which the followers must be fetched
UpdateFollowers(acc_screen_name)
