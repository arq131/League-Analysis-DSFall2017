import json
import os
import pandas as pd


df = pd.DataFrame(columns=['Title', 'Date Created', 'If Self-post', 'Score'])

with open('leagueoflegendsNov\merged_file.json', 'r') as data_file:
        data = json.load(data_file)

# Change to data[0] for Nov. data set, idk why it's nested in another node
for row in data[0]:
    rowframe = pd.DataFrame([[row[0]['data']['children'][0]['data']['title'].encode('ascii', 'ignore'),
                             row[0]['data']['children'][0]['data']['created'],
                             row[0]['data']['children'][0]['data']['is_self'],
                             row[0]['data']['children'][0]['data']['score']]], columns=['Title', 'Date Created', 'If Self-post', 'Score'])
    df = pd.concat([df, rowframe], ignore_index=True)


df['Date Created'] =  pd.to_datetime(df['Date Created'], unit='s')

df.to_csv('submissionDataNovFinal.csv')
