import requests
import csv
import json

count = "150"

#test parsing
r = requests.get(url='https://reddit.com/r/roastme/top/.json?limit='+ count +'&t=all', headers = {'User-agent': 'XynoBot'})
with open('metadata.json', 'w') as outfile:
    json.dump(r.json(), outfile)
for item in r.json()['data']['children']:
    print(item['data']['url'])
dataDump = open('DataDump.csv', 'w')
csvwriter = csv.writer(dataDump)
csvwriter.writerow(['id', 'title', 'comments', 'url'])
for item in r.json()['data']['children']:
    itemID = item['data']['id']
    itemTitle = item['data']['title']
    itemComments = item['data']['permalink']
    itemLink = item['data']['url']
    row = [itemID, itemTitle, itemComments, itemLink]
    csvwriter.writerow(row)
dataDump.close()

