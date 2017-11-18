import json
import os
import pandas as pd


df = pd.DataFrame(columns=['Title', 'Date Created', 'If Self-post'])

with open('leagueoflegendsOct\merged_file.json', 'r') as data_file:
        data = json.load(data_file)

for row in data:
    rowframe = pd.DataFrame([[row[0]['data']['children'][0]['data']['title'].encode('ascii', 'ignore'),
                             row[0]['data']['children'][0]['data']['created_utc'],
                             row[0]['data']['children'][0]['data']['is_self']]], columns=['Title', 'Date Created', 'If Self-post'])
    df = pd.concat([df, rowframe], ignore_index=True)


df.to_csv('submissionDataOct.csv')
