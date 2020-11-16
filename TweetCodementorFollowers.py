import tweepy  #pip install tweepy
import csv
import random
import time

#D Shekhar's acc: creds
consumer_key = "qMWbJWBrlTt12JgeoItg3OPal"
consumer_secret = "j1egFweAOq61ViTro9s7EmfSlCYapLdKWfqm87s3YRU6kzeMLG"
access_token = "1323515644029988871-IiCUtSsTeMEBUURUv0k3vEySI6gYJN"
access_token_secret = "3F2bhwEm4K1zHW6PgMikKFNshUt8dTAZXIt7mIkm9tK57"

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
