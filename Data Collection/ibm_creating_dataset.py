import GetOldTweets3 as got
import pandas as pd
import tweepy
from datetime import date as date_
import requests 
import csv

d0 = date_(2020, 3, 14) # date representing initial date from which data is there for corona cases

region=["KL","MH","RJ","KA","GA","MP","UP","GJ","TN","TS","BH","JK","PY","HR","AP","WB","CT","OR","JH","AS","HP","NL","SK","MN","AR","TR","ME","MI","UT"] #statecode corresponding to particular coordinates and radius
coordinates=["10.8505,76.2711","19.7515,75.7319","27.0238,74.2179","15.3173,75.7139","15.2993,74.1240","22.9734,78.6569","28.8467,80.9462","22.2587,71.1924","11.1271,78.6569","18.1124,79.0193","25.0961,85.3131","33.7782,76.5762","31.1471,75.3412","29.0588,76.0856","15.9129,79.7400","22.9868,87.8550","21.2787,81.8661","20.9517,85.0985","23.6102,85.2799","26.2006,92.9376","31.1048,77.1734","26.1584,94.5624","27.5330,88.5122","24.6637,93.9063","28.2180,94.7278","23.9408,91.9882","25.4670,91.3662","23.1645,92.9376","30.0668,79.0193"]
radius=["111.22","312.97","330.05","247.08","34.33","313.29","278.28","249.79","203.47","188.88","173.12","115.95","126.61","118.63","227.76","168.07","207.44","222.62","159.29","158.01","133.12","72.64","47.52","84.30","163.26","57.77","84.49","81.92","130.47"]

consumer_key="HBphkAktZUCXnzsETAL2DZDZ5"
consumer_secret="RVI25oLDDIHnwdlDTetMKkreG40tM0JLESP2rtMvjMr3SvbeQS"
access_token="1249603598545113089-JBOA1Bg2drujYFJbXL2ODAeL8lWX9v"
access_token_secret="TBZ2t8xOoHvdL2tuFArMsQrcjIFBOn33IO1v7Bs1FGP5r"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

f=open("dataset_actual.csv","w", encoding='utf-8')
w = csv.writer(f,lineterminator='\n')
data = pd.read_csv('data.csv', sep=',', header=None) #daily increase in corona cases dataset

def get_row_col(data,state,date):
	col=data.index(state.lower())
	date1=[]
	date1=date.split("/")
	d1=date_(int(str(date1[2])),int(str(date1[1])),int(str(date1[0])))
	row=(d1-d0).days
	row+=1

	return row,col
	
data_cases=list(data.iloc[0])
for i in range(0,len(region)):
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#covid19 #coronavirus #lockdown').setSince("2020-03-01").setUntil("2020-05-31").setNear(coordinates[i]).setWithin(radius[i]+"km").setMaxTweets(200)
	tweets = got.manager.TweetManager.getTweets(tweetCriteria)
	# print(tweets)
	for tweet in tweets:
		user=api.get_user(tweet.username)
		print(user.name)
		if len(user.name.split(" "))>1: # GENDER API requires atleast first and last name 
			name=user.name.split(" ")
			date=str(str(tweet.date.day)+"/"+str(tweet.date.month)+"/"+str(tweet.date.year))
			gender=requests.get('http://api.namsor.com/onomastics/api/json/gender/'+name[0]+'/'+name[1]).json()['gender']
			state=region[i]
			index_=get_row_col(data_cases,state,date) # get row and col representing cororna cases on particular date and in given state
			cases=data.iloc[index_[0],index_[1]]
			write_data=[date,user.name,gender,tweet.text,tweet.retweets,state,cases]
			w.writerow(write_data)

