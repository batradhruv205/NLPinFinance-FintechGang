# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:36:53 2019
Make data more useable
@author: batra
"""
import pandas as pd

SubmissionsTick = pd.read_csv('Output/SubmissionsTick7_0.csv')
SubmissionsName = pd.read_csv('Output/SubmissionsName7_0.csv')

Submissions = pd.DataFrame()
Submissions = Submissions.append(SubmissionsTick)
Submissions = Submissions.append(SubmissionsName, ignore_index=True)
Submissions['PostId'] = ""
for i in Submissions.index:
    Submissions['PostId'][i] = Submissions['INDEX'][i] + Submissions['id'][i]

Submissions = Submissions.drop_duplicates(subset = 'PostId')
Submissions.drop(Submissions[Submissions['num_comments']<1].index, inplace = True)

Submissions['selftext'] = Submissions['selftext'].astype(str)

Submissions['Text'] = ""
for i in Submissions.index:
    Submissions['Text'][i] = Submissions['post_title'][i] + " " + \
    Submissions['selftext'][i] + " " + Submissions['comments'][i]
    
Submissions = Submissions.drop(columns = ['selftext','comments','post_title'])
Submissions.to_csv('Output/Corpus.csv', index=None)
# Ready to process text

