import os
import pandas as pd
import tweepy
import re
import string
from textblob import TextBlob
import preprocessor as p
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tweepy
import datetime
import xlsxwriter
import sys
from tweepy.cursor import Cursor
import random



consumer_key = 'XoZtI33j0N2rXgo7RoV2WkRA8'
consumer_secret = 'GhTZoc72V86cPNS4XwmhEQgXpfMIP5bf67xjyY4P4BDsdtwsFq'
access_token = '1169123246421229568-E2afs7vzy5VybyAtsPtUE0bZNr90hI'
access_token_secret = 'qFCos7kbfXH2MiwrGIZ9yeZbMRp3J7zLyQZluOEMeHwwX'



# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# # Number of tweets to pull
tweetCount = 1000

# Creating the API object while passing in auth information
# api = tweepy.API(auth)

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

# The search term you want to find
r=""
for x in range(1):
  k=random.randint(1000,9999)
  r=r+str(k)
Keyword=input("enter keyword :")
query = "#"+Keyword
# Language code (follows ISO 639-1 standards)
language = "en"
Filename=Keyword+r
print("filename is",Filename)

# Keyword="Coffee"
# query = "#"+Keyword
# Filename=Keyword+"2"
# Language code (follows ISO 639-1 standards)
# language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language,count=tweetCount)

# foreach through all tweets pulled
# for tweet in results:
#    # printing the text stored inside the tweet object
#    print ({"User name":tweet.user.screen_name,"Tweeted":tweet.text,"tweet created at":tweet.created_at})


workbook = xlsxwriter.Workbook(Filename + ".xlsx")
worksheet = workbook.add_worksheet()
row = 1
worksheet.write('A1', 'User Name') 
worksheet.write('B1', 'Created time') 
worksheet.write('C1', 'Tweet') 
worksheet.write('D1', 'Reply status_id')
worksheet.write('E1', 'Location of tweet')
worksheet.write('F1', 'Favorite Count')
worksheet.write('G1', 'Retweet Count')
worksheet.write('H1', 'Followers')

for tweet in results:
    worksheet.write_string(row, 0, str(tweet.user.screen_name))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    worksheet.write_string(row, 4, str(tweet.user.location))
    worksheet.write_string(row, 5, str(tweet.favorite_count))
    worksheet.write_string(row, 6, str(tweet.retweet_count))
    worksheet.write_string(row, 7, str(tweet.user.followers_count))

    row += 1

workbook.close()
print("Excel file ready")

# result1 = Cursor(api.search,q=query,since="2014-01-01",until="2014-01-02",lang="en").items()
# print(result1)
# for tweet in result1:
#     print((tweet))
# for tweet in Cursor(api.search,q="test",since="2014-01-01",until="2014-01-02",lang="en").items():
#     print(tweet)

# for tweet in tweepy.Cursor(api.search,q="Coffee",since="2018-01-01",until="2019-02-01",lang="en").items():
#     print(tweet)
 