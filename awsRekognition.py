import urllib.request
import boto3
import os
import csv
import json
import pandas as pd
import jsonToCsv

df = pd.read_csv('DataDump.csv')
links = df.url
ids = df.id
count = 0
os.makedirs("AWS", exist_ok=True)
dataDump = open('AWS/DataDump.csv', 'w')
csvwriter = csv.writer(dataDump)
for link in links:
    if link[-3:] == "jpg":
        print(link)
        urllib.request.urlretrieve(link, "/home/gokul/Pictures/roast.jpg")
        imageFile='/home/gokul/Pictures/roast.jpg'
        client=boto3.client('rekognition')
        
        with open(imageFile, 'rb') as image:
            response = client.detect_faces(Image={'Bytes': image.read()}, Attributes = ["ALL"])
            with open('AWS/'+ids[count]+'.json', 'w') as outfile:
                json.dump(response, outfile)
            row = [ids[count], link]
            if count == 0:
               	titles = ["id", "url"]
               	jsonToCsv.getTitles(titles, response["FaceDetails"][0], "")
               	csvwriter.writerow(titles)
            count += 1
            if response["FaceDetails"]:
               	jsonToCsv.flatten(row, response["FaceDetails"][0])
               	csvwriter.writerow(row)
print('Done...')
