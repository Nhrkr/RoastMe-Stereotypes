import requests
import csv
import json

#test parsing
r = requests.get(url='https://reddit.com/r/roastme/top/.json?limit=20&t=all', headers = {'User-agent': 'XynoBot'})
with open('metadata.json', 'w') as outfile:
    json.dump(r.json(), outfile)
for item in r.json()['data']['children']:
    print(item['data']['url'])
dataDump = open('DataDump.csv', 'w')
csvwriter = csv.writer(dataDump)
count = 0
for item in r.json()['data']['children']:
    if count == 0:
        csvwriter.writerow(item['data'].keys())
        count += 1
    csvwriter.writerow((item['data'].values()))
dataDump.close()

