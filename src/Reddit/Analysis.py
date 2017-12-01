import pandas as pd

df = pd.DataFrame.from_csv('submissionDataFinal.csv')

# Rows containing KeyWords
kwPatch = df[df['Title'].str.contains('patch')]
kwPreseason = df[df['Title'].str.contains('preseason')]
kwMastery = df[df['Title'].str.contains('masteries')]
kwRunes = df[df['Title'].str.contains('rune')]

kwPatchFreq = kwPatch['Title'].count()
kwPreseasonFreq = kwPreseason['Title'].count()
kwMasteryFreq = kwMastery['Title'].count()
kwRunesFreq = kwRunes['Title'].count()

# Sum of voting scores for keyword rows
kwPatchScore = kwPatch['Score'].sum()
kwPreseasonScore = kwPreseason['Score'].sum()
kwMasteryScore = kwMastery['Score'].sum()
kwRunesScore = kwRunes['Score'].sum()

kwData = {'Patch': [kwPatchFreq], 'Pre-season': [kwPreseasonFreq], 'Masteries': [kwMasteryFreq], 'Runes': [kwRunesFreq]}
kwHist = pd.DataFrame(data=kwData)

kwHist.diff().hist()
