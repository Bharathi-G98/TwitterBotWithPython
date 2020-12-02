import json
import time
import csv
from flask import Flask, request
import mysql.connector
import datetime
import time


app = Flask(__name__)


def OAuth(consumer_key,consumer_secret,access_token,access_token_secret):
 try:
  auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
  auth.set_access_token(access_token,access_token_secret)
  return auth
 except Exception as e:
  print("error")

def PostTweet(message):
 api.update_status(message)
 print("tweet has been posted")
 
def GetFollowers(acc_screen_name,api):
 follower_count=api.get_user(acc_screen_name).followers_count
 count=1
 limit=random. randint(250,300)
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 for follower in tweepy.Cursor(api.followers, acc_screen_name).items(follower_count):
  if count==limit:
   sl=random. randint(900,1800)
   print("about to sleep for"+str(sl)+"seconds")
   time.sleep(sl)
   limit+=random. randint(250,300)
  data=[]
  print(count)
  try:
   sql = "INSERT INTO "+handle[1:]+" (username) VALUES (%s)"
   val = ('@'+follower.screen_name,)
   cur.execute(sql, val)
   conn.commit()
  except:
   conn.rollback()
   pass
  count+=1

def createCompetitor(data,api):
 #creating table with name handle
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 handle=data["handle"]
 cur.execute("CREATE TABLE IF NOT EXISTS " + handle[1:] + " (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(100))")
 result = cur.fetchall()
 conn.close()
 #fetching all followers and storing into handle table
 GetFollowers(handle,api)

 
 
 
def launch(data):
 #!TODO
 #checking if acc exists
 consumer_key = data['consumer_key']
 consumer_secret = data["consumer_secret"]
 access_token = data["access_token"]
 access_token_secret = data["access_token_secret"]
 
 oAuth = OAuth(consumer_key,consumer_secret,access_token,access_token_secret)
 api = tweepy.API(oAuth,wait_on_rate_limit = True)
 
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 cur.execute("SELECT consumer_key FROM Accounts")
 result = cur.fetchall()
 res=[i[0] for i in result]
 conn.close()
 
 if consumer_key not in res:
  return "This account is a new account. Please hit new acc api."
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 sql= '''SELECT status FROM Accounts WHERE consumer_key = %s'''
 val = (consumer_key,)
 result = cur.fetchall()
 conn.close()
 if result[0] == "active:
  return "account is already being used"
 
  
 
 #get all rows of comp
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 sql = '''SELECT name from Competitors'''
 cur.execute(sql)
 result = cur.fetchall()
 conn.close()
 compet = [i[0] for i in result]
 
 #check if handle table with followers exists
 if handle[1:] not in comp:
  createCompetitor(data,api)
 
 #FETCH FOLLOWERS OF HANDLE
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 handle=data["handle"]
 cur.execute("SELECT username from " + handle[1:])
 result = cur.fetchall()
 conn.close()
 toTweet = i[0] for i in result]
 
 #FETCH RandMessageIds
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 sql = '''SELECT msgId from RandMessagesIds'''
 cur.execute(sql)
 result = cur.fetchall()
 conn.close()
 randMessages = [i[0] for i in result]
 
 #FETCH MESSAGES TO BE TWEETED
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 sql = '''SELECT message from Messages'''
 cur.execute(sql)
 result = cur.fetchall()
 conn.close()
 messages = [i[0] for i in result]
 
#start tweeting,following and retweeting
 randMsgTweeted=[]
 usersFollowed=[]
 limit=20
 randMsg=8
 for i in range(len(toTweet)):
  if i==limit:
   s=random. randint(300,900)
   #select rand competitor
   randComp=compet[random. randint(0,len(compet)-1)]
   #FETCH FOLLOWERS OF COMP
   conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
   cur = conn.cursor()
   handle=data["handle"]
   cur.execute("SELECT username from " + randComp)
   result = cur.fetchall()
   conn.close()
   #select a user that has not been followed
   users = i[0] for i in result]  
   user=users[random. randint(0,len(users)-1)]
   if usersFollowed:
    while user in usersFollowed:
     conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
     cur = conn.cursor()
     handle=data["handle"]
     cur.execute("SELECT username from " + randComp)
     result = cur.fetchall()
     conn.close()
     users = i[0] for i in result]  
     user=users[random. randint(0,len(users)-1)]
   usersFollowed.append(user)
   try:
    api.create_friendship(user)
    time.sleep(s)
   except:
    print("============================in follow except")
    pass 
   limit+=random. randint(12,20)
  #retweet a random tweet
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
  #tweet targetting user
  mInd=random. randint(0,len(messages)-1)
  message=messages[mInd].replace("@username",toTweet[i])
  message=message.replace("crewscale.com","https://bit.ly/2TKjx9V")
  try:
   api.update_status(message)
   sl=random. randint(1800,3600)
   print("about to sleep for"+str(sl)+"seconds")
   time.sleep(sl)
  except:
   print("========================================in post tweet except")
   pass
 
 #account added to Accounts entity, tweets from NewAccMessages tweeted till acc temporarily blocked.
@app.route("/newAccount",methods=['POST'])
def newAcc():
 data=request.get_json()
 consumer_key = data['consumer_key']
 consumer_secret = data["consumer_secret"]
 access_token = data["access_token"]
 access_token_secret = data["access_token_secret"]
 
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 cur.execute("SELECT consumer_key FROM Accounts")
 result = cur.fetchall()
 res=[i[0] for i in result]
 conn.close()
 
 if consumer_key in res:
  return "This account is not a new account and already has been used."
 
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 insert_stmt = (
                     "INSERT INTO Accounts(consumer_key,consumer_secret,access_token,access_token_secret,status)"
                     "VALUES (%s, %s, %s, %s, %s)"
                       )
 data = (consumer_key,consumer_secret,access_token,access_token_secret,"inactive")
 try:
  cur.execute(insert_stmt, data)
  conn.commit()
  print("Data inserted")
 except:
  return "account updation did not happen, something went wrong. Please try again."
  conn.rollback()
  pass
 conn.close()
 
 oAuth = OAuth(consumer_key,consumer_secret,access_token,access_token_secret)
 api = tweepy.API(oAuth,wait_on_rate_limit = True)
 
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 sql = '''SELECT message from NewAccMessages'''
 cur.execute(sql)
 result = cur.fetchall()
 conn.close()
 r=[i[0] for i in result]
 
 conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
 cur = conn.cursor()
 sql = '''UPDATE Accounts SET status = 'active' WHERE consumer_key = %s'''
 val = (consumer_key,)
 try:
  cur.execute(sql, val)
  conn.commit()
  print("Data inserted")
 except:
  conn.rollback()
 conn.close()
 
 for m in r:
  try:
   api.update_status(message)
   sl=random. randint(1800,3600)
   print("about to sleep for"+str(sl)+"seconds")
   time.sleep(sl)
  except:
   conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='twitter')
   cur = conn.cursor()
   sql = '''UPDATE Accounts SET status = 'inactive' WHERE consumer_key = %s'''
   val = (consumer_key,)
   try:
    cur.execute(sql, val)
    conn.commit()
    print("Data inserted")
   except:
    conn.rollback()
   conn.close()
   return "Please verify your number and unblock your account. Now you can use this account to tweet followers."

 
#this api shopuld only be hit if account already verified. 
@app.route("/launchCampaign",methods=['POST'])
def getRequest():
    #print(request.form.get("handle")) #for req param
    data=request.get_json()
    launch(data)
    print(data["handle"]) #for request body
    
    return "done"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80, threaded=True)
