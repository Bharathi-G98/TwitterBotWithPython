
***Prerequisites: 
>python 3.6,
>MySql5.7,
>tweepy,
>flask


->FOR RUNNING twitterCampaignModule.py

*Command to run: 

sudo python twitterCampaignModule.py >> Twitterlog.txt 2>&1 &

*Queries:

>create database twitter;
>CREATE TABLE Competitors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));
>CREATE TABLE Accounts (id INT AUTO_INCREMENT PRIMARY KEY, consumer_key VARCHAR(255), consumer_secret VARCHAR(255), access_token VARCHAR(255), access_token_secret VARCHAR(255), status VARCHAR(50));
>CREATE TABLE NewAccMessages (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(700));   (must be poplulated before running code.)
>CREATE TABLE RandMessagesIds(id INT AUTO_INCREMENT PRIMARY KEY, msgId VARCHAR(700));     (must be poplulated before running code. run getTweetIdsForHastag.py to do so)
>CREATE TABLE Messages (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(700));          (must be poplulated before running code.)


*Essential Components:

>database named twitter
>>ENTITIES:
-Accounts: contains acc creds and status
-Competitors: names of all competitors whose followers have been fetched.
-NewAccMessages: populate this table with about 100 messages. These messages will be tweeted from a new account until it is temporarily blocked and phone number needs to be verified. 
-RandMessagesIds: contains tweet ids of tweets to be retweeted
-Messages : contains tweets targetting each user.

*Note: in the post request, along with account creds, handle should be @something

*HOW TO USE:

>if you are using a new account, hit /newAccount. Include the credentials in the request body.
>wait till you recieve the response indicating your account has been temporarily blocked and verify your number.
>Now, you can hit /launchCampaign. Include your account credentials along with the twitter handle of the account whose followers must be targetted. If the account is inactive, the process will commence.
>in arbitrary intervals, messages will be tweeted, tweets will be retweeted and followers of twitter handles that exist in the database will be followed. 

--> Alternatively, genericGetFollowers.py can be used to fetch and store followers in a csv file and tweetGeneric.py can be used to tweet, targetting the same.
