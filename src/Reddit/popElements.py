import json
import os

filenameList = []

def popElement(directory, filename, element):
    with open(directory + '/' + filename, 'r') as data_file:
        data = json.load(data_file)
    # try:
    #     data[1]
    # except IndexError:
    #     filenameList.append(filename)
    data.pop(element)
    with open(directory + '/' + filename, 'w') as data_file:
        data = json.dump(data, data_file)
    print filename

for file in os.listdir('leagueoflegendsOct'):
    popElement('leagueoflegendsOct', file, 1)

print len(filenameList)
