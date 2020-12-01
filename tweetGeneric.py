import tweepy  #pip install tweepy
import csv
import random
import time

"""
HOW THIS CODE WORKS:
-the list: "competitors" contains names of all competitors other than the one whose followers are currently to be tweeted.
-each individual competitor's followers are fetched and stored in respective lists.
- the list "messages" contains the messages to be tweeted targetting followers.
- the list "randMessages" contains tweet ids of tweets related to #remote
INSIDE UpdateFollowers
-the list "randMsgTweeted" conatins indices of ids in randMessages that have been tweeted.
-the list "usersFollowed" contains all users that have been followed 
-iterating through all followers of current competitor to be tweeted:
 >if i== limit (increased in random intervals), follow random user of random competitor (not the one being tweeted), user added to usersFollowed
 >if i == randMsg (increased in random intervals), radmon tweet id from radnMessages list will be retweeted, and id will be added to randMessages
 >tweet user and sleep for random time
 
"""


#account's credentials : available on twitter dashboard, when you select the app and go to keys and tokens
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
 limit=20
 randMsg=8
 for i in range(len(remoteokFollowers)):
  if i==limit:
   s=random. randint(300,900)
   comp=competitors[random. randint(0,len(competitors)-1)]
   user=comp[random. randint(0,len(comp)-1)]
   if usersFollowed:
    while user in usersFollowed:
     comp=competitors[random. randint(0,len(competitors)-1)]
     user=comp[random. randint(0,len(comp)-1)]
   usersFollowed.append(user)
   try:
    api.create_friendship(user)
    time.sleep(s)
   except:
    print("============================in folow except")
    pass 
   limit+=random. randint(12,20)
  if i==randMsg:
    mInd=random. randint(0,len(randMessages)-1)
    if randMsgTweeted:
     while mInd in randMsgTweeted:
      mInd=random. randint(0,len(randMessages)-1)
    randMsgTweeted.append(mInd)
    mes=randMessages[mInd]
    try:
     api.retweet(mes)
     sl=random. randint(300,900)
     time.sleep(sl)
    except:
     print("============================in rand msg except")
     pass 
    randMsg+=random. randint(10,15)
  mInd=random. randint(0,len(messages)-1)
  message=messages[mInd].replace("@username",remoteokFollowers[i])
  message=message.replace("crewscale.com","https://bit.ly/2TKjx9V")
  try:
   api.update_status(message)
   sl=random. randint(1800,3600)
   print("about to sleep for"+str(sl)+"seconds")
   time.sleep(sl)
  except:
   print("========================================in post tweet except")
   pass

competitors=[]

remoteokFollowers=[]
with open('/home/ubuntu/Twitter/@RemoteOKFollowers.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        remoteokFollowers.append(row[0])
remoteokFollowers=remoteokFollowers[1:]
#competitors.append(remoteokFollowers)

codementorFollowers=[]
with open('/home/ubuntu/Twitter/@CodementorIOFollowers.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        codementorFollowers.append(row[0])
codementorFollowers=codementorFollowers[1:]
competitors.append(codementorFollowers)

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
with open('/home/ubuntu/Twitter/remoteIds.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        randMessages.append(row[0])
randMessages=randMessages[1:]
oAuth = OAuth()
api = tweepy.API(oAuth,wait_on_rate_limit = True)
acc_screen_name = "@CodementorIO"   #the user screen name for which the followers must be fetched
#image_path="C://Users//Lenovo//Downloads//crewscale.jpeg"
UpdateFollowers(acc_screen_name)
