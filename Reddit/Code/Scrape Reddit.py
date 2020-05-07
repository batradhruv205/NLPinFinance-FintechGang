es # -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:55:21 2019

@author: batra
"""

#Environment
import pandas as pd
import datetime as dt
import praw


##Raw Data
rawdata = pd.read_csv("Input/2018_final_earnings_release.csv")
#Remove extra columns
rawdata = pd.DataFrame.drop(rawdata, columns=\
                            ["epsactual","epsestimate","epssurprisepct",\
                             "gmtOffsetMilliSeconds","quoteType","startdatetimetype","is_sp500"])
#Create Date Column for data mining
rawdata['date'] = [pd.to_datetime(x[0:10]) for x in rawdata['startdatetime']]


##Data to Mine
# generate a dataframe that has the ticker, start date and end date.
datatomine = pd.DataFrame.drop(rawdata, columns=["startdatetime"])
# create start and end dates
dup = dt.timedelta(days=0)
ddwn = dt.timedelta(days=-7)
datatomine['enddt']=[x+dup for x in datatomine['date']]
datatomine['strtdt']=[x+ddwn for x in datatomine['date']]
        
        
# use PRAW to obtain reddit objects
reddit = praw.Reddit(client_id='TweKypXogoSgLg',
              client_secret="MqbbXM9ZY2AEnHk1-UuqrmtyUxM", 
              user_agent='Python (by NotAThrowaway205)')
subredinvest = reddit.subreddit('investing')

Posts = pd.DataFrame(columns = ['INDEX','id', 'post_title','created_at',\
                                'num_comments','score','selftext',\
                                'upvote_ratio','comments'])


## Class for reddit objects
class redditobj:
    def __init__(self, index, submission):
        self.index=index
        self.submission=submission
        
        
# Below block uses ticker names
submissionstick = []
for x in range(0,len(datatomine)):
    print (x)
    for i in subredinvest.search(datatomine['ticker'][x]):
        if datatomine['enddt'][x].to_pydatetime() >= dt.datetime.fromtimestamp(i.created_utc) >=                         datatomine['strtdt'][x].to_pydatetime():
            submissionstick.append(redditobj(datatomine['Index'][x],i))


for i in submissionstick:
    comments =[]
    for j in i.submission.comments:
        if isinstance(j, praw.models.MoreComments):
            continue
        comments.append(j.body)
    data = pd.DataFrame([[i.index,i.submission.id,i.submission.title,\
                         i.submission.created_utc,i.submission.num_comments,\
                         i.submission.score,i.submission.selftext,\
                         i.submission.upvote_ratio,comments]])
    data.columns = ['INDEX','id', 'post_title','created_at','num_comments','score','selftext','upvote_ratio','comments']
    Posts=Posts.append(data)

Posts.to_csv("Output/SubmissionsTick7_0.csv", index=None)


Posts = pd.DataFrame(columns = ['INDEX','id', 'post_title','created_at',\
                                'num_comments','score','selftext',\
                                'upvote_ratio','comments'])
# Below block uses the company short name
submissionsnam = []
for x in range(0,len(datatomine)):
    print (x)
    for i in subredinvest.search(datatomine['companyshortname'][x]):
        if datatomine['enddt'][x].to_pydatetime() >= dt.datetime.fromtimestamp(i.created_utc) >= datatomine['strtdt'][x].to_pydatetime():
            submissionsnam.append(redditobj(datatomine['Index'][x],i))

for i in submissionsnam:
    comments =[]
    for j in i.submission.comments:
        if isinstance(j, praw.models.MoreComments):
            continue
        comments.append(j.body)
    data = pd.DataFrame([[i.index,i.submission.id,i.submission.title,\
                         i.submission.created_utc,i.submission.num_comments,\
                         i.submission.score,i.submission.selftext,\
                         i.submission.upvote_ratio,comments]])
    data.columns = ['INDEX','id', 'post_title','created_at','num_comments','score','selftext','upvote_ratio','comments']
    Posts=Posts.append(data)

Posts.to_csv("Output/SubmissionsName7_0.csv", index=None)

###
# Next step will be to group the data by INDEX.
# Then, group the data by submission ID
# Keep only one row for each ID/Index pair
# Somehow remove irrelevant posts (or not?)
# Then do TA on Comments column. Produce a sentiment score from there.
# Using the sentiment score on comments and the submission title+body, generate a submission sentimennt score
# Generate a sentiment score for each Index.