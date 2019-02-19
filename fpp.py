import requests
import os
import csv
import json
import pandas as pd
import jsonToCsv

df = pd.read_csv('DataDump.csv')
links = df.url
ids = df.id
count = 0
os.makedirs("faceplusplus", exist_ok=True)
dataDump = open('faceplusplus/DataDump.csv', 'w')
csvwriter = csv.writer(dataDump)
for link in links:
    if link[-3:] == "jpg":
        print(link)
        with open('faceplusplus/apiKey', 'r') as myfile:
            apiKey = myfile.read().replace('\n', '')
        with open('faceplusplus/apiSecret', 'r') as myfile:
            apiSecret = myfile.read().replace('\n', '')
        analyze_url = "https://api-us.faceplusplus.com/facepp/v3/detect"
        params     = {'api_key': apiKey, 'api_secret': apiSecret, 'image_url': link, 'return_attributes': 'gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,eyestatus,skinstatus'}
        try:
            response = requests.post(analyze_url, params = params)
            response.raise_for_status()
            analysis = response.json()
            with open('faceplusplus/'+ids[count]+'.json', 'w') as outfile:
                json.dump(analysis, outfile)
            row = [ids[count], link]
            if count == 0:
                titles = ["id", "url"]
                jsonToCsv.getTitles(titles, analysis["faces"][0]["attributes"], "")
                csvwriter.writerow(titles)
                count += 1
            if analysis["faces"]:
                jsonToCsv.flatten(row, analysis["faces"][0]["attributes"])
                csvwriter.writerow(row)
        except requests.exceptions.HTTPError as e:
            print(e)
dataDump.close()

