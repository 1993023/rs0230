#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import datetime
import xlsxwriter
import sys
import random

# credentials from https://apps.twitter.com/
# consumerKey = "CONSUMER_KEY"
# consumerSecret = "CONSUMER_SECRET"
# accessToken = "ACCESS_TOKEN"
# accessTokenSecret = "ACCESS_TOKEN_SECRET"

consumerKey = 'XoZtI33j0N2rXgo7RoV2WkRA8'
consumerSecret = 'GhTZoc72V86cPNS4XwmhEQgXpfMIP5bf67xjyY4P4BDsdtwsFq'
accessToken = '1169123246421229568-E2afs7vzy5VybyAtsPtUE0bZNr90hI'
accessTokenSecret = 'qFCos7kbfXH2MiwrGIZ9yeZbMRp3J7zLyQZluOEMeHwwX'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

# username = sys.argv[1]
r=""
for x in range(1):
  k=random.randint(1000,9999)
  r=r+str(k)
username=input("enter keyword :")
Keyword=username
query = "#"+Keyword
# Language code (follows ISO 639-1 standards)
language = "en"
filename=username+r
print("filename is",filename)

# username="Olam"
# filename=username+""
startDate = datetime.datetime(2017, 7, 1, 0, 0, 0)
endDate =   datetime.datetime(2019, 1, 1, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

workbook = xlsxwriter.Workbook(filename + ".xlsx")
worksheet = workbook.add_worksheet()
row = 1
worksheet.write('A1', 'User Name') 
worksheet.write('B1', 'Created time') 
worksheet.write('C1', 'Tweet') 
worksheet.write('D1', 'Reply status_id')
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.user.screen_name))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    row += 1

workbook.close()
print("Excel file ready")