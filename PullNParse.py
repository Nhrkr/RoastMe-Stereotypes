import requests
import csv
import json

count = "100"

dataDump = open('DataDump.csv', 'w')
csvwriter = csv.writer(dataDump)
csvwriter.writerow(['id', 'title', 'comments', 'url'])
session = requests.session()
for turn in range(3):
    if turn == 0:
        r = session.get(url='https://reddit.com/r/roastme/top/.json?limit='+ count + '&t=all', headers = {'User-agent': 'XynoBot'})
    else:
        r = session.get(url='https://reddit.com/r/roastme/top/.json?limit='+ count + '&t=all&after=' + name, headers = {'User-agent': 'XynoBot'})
    with open('metadata' + str(turn) + '.json', 'w') as outfile:
        json.dump(r.json(), outfile)
    for item in r.json()['data']['children']:
        print(item['data']['url'])
    for item in r.json()['data']['children']:
        itemID = item['data']['id']
        itemTitle = item['data']['title']
        itemComments = item['data']['permalink']
        itemLink = item['data']['url']
        name = item['data']['name']
        row = [itemID, itemTitle, itemComments, itemLink]
        csvwriter.writerow(row)
dataDump.close()

