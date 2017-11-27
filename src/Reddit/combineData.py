import json
import os
import pandas as pd


dfOct = pd.DataFrame(columns=['Title', 'Date Created', 'If Self-post', 'Score'])
dfNov = pd.DataFrame(columns=['Title', 'Date Created', 'If Self-post', 'Score'])
dfFinal = pd.DataFrame(columns=['Title', 'Date Created', 'If Self-post', 'Score'])

dfOct = pd.DataFrame.from_csv('submissionDataOctFinal.csv')
dfNov = pd.DataFrame.from_csv('submissionDataNovFinal.csv')

dfFinal = dfOct.append(dfNov, ignore_index=True)

dfFinal.to_csv('submissionDataFinal.csv')
