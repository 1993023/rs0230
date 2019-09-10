import os
import pandas as pd
import tweepy
import re
from textblob import TextBlob
import tweepy
import datetime
import time
import xlsxwriter
import sys
from tweepy.cursor import Cursor
import random
from requests.exceptions import Timeout,ConnectionError




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
# ["Sustainability","Sustainable farming","Clean labels","Organic farming"]
Industry_list=["Farming","Environment","Climate change","Global Warming","Agriculture","Fair trade","Recycling","Carbon footprint","Pollution","Pesticides","Plastic","Plastic waste","Water","Earth","Nature","Waste Management","Deforestation","Greenhouse gases","Organic food","Conservation","GMO","Recycling","Packaging"]

# Industry_list=["Wholesome Bars","Muesli"]
filename_list=[]

for i in range(len(Industry_list)):

    r=""
    for x in range(1):
        k=random.randint(1000,9999)
        r=r+str(k)
    Keyword=Industry_list[i]
    # query = "#"+Keyword
    query = Keyword or "#"+Keyword
    # Language code (follows ISO 639-1 standards)
    language = "en"
    Filename=Keyword+r
    # print("filename is",Filename)
    filename_list.append(Filename)
    workbook = xlsxwriter.Workbook("Industry/"+Filename + ".xlsx")
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


    try:
        for tweet in tweepy.Cursor(api.search,q=query,
                                lang="en",
                                since="2019-07-02",until="2019-09-10").items():
            print (tweet.created_at, tweet.text)
            worksheet.write_string(row, 0, str(tweet.user.screen_name))
            worksheet.write_string(row, 1, str(tweet.created_at))
            worksheet.write(row, 2, tweet.text)
            worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id)) 
            worksheet.write_string(row, 4, str(tweet.user.location))
            worksheet.write_string(row, 5, str(tweet.favorite_count))
            worksheet.write_string(row, 6, str(tweet.retweet_count))
            worksheet.write_string(row, 7, str(tweet.user.followers_count))

            row += 1
       
    except:
        time.sleep(180)
    finally:
        workbook.close()
        # print("filename is",Filename)
        print(Filename,"Excel file ready")
    

print("filename is",filename_list)
 