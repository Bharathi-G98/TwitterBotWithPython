import tweepy  #pip install tweepy
import csv
import random
import time

#this populates a csv as well as an entity called RandMessagesIds in a database called Twitter

csvFile = open('remoteNewIds.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
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
oAuth = OAuth()
api = tweepy.API(oAuth,wait_on_rate_limit = True)

forCsv=[]
for tweet in tweepy.Cursor(api.search,q="#productivity",count=5000,
                           lang="en",
                           since="2017-04-03").items():
    forCsv.append([tweet.id])

csvWriter.writerows(forCsv)

forDb=[i[0] for i in forCsv]
for i in forDb:
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 sql = "INSERT INTO RandMessagesIds (msgId) VALUES (%s)"
 val = (i,)
 cur.execute(sql, val)
 conn.commit()
 conn.close()

