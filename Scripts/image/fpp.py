import requests
import os
import csv
import json
import pandas as pd
import jsonToCsv
import time

def getData(analyze_url, params, ids, count, csvwriter):
    try:
        response = requests.post(analyze_url, params = params)
        response.raise_for_status()
        analysis = response.json()
        with open('../../Data/image/faceplusplus/'+ids[count]+'.json', 'w') as outfile:
            json.dump(analysis, outfile)
        row = [ids[count], link]
        if count == 0:
            titles = ["id", "url"]
            jsonToCsv.getTitles(titles, analysis["faces"][0]["attributes"], "")
            csvwriter.writerow(titles)
        if analysis["faces"]:
            jsonToCsv.flatten(row, analysis["faces"][0]["attributes"])
            csvwriter.writerow(row)
    except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                print("retrying for " + link)
                getData(analyze_url, params, ids, count, csvwriter)
            print(e)


df = pd.read_csv('../../Data/image/DataDump.csv')
links = df.url
ids = df.id
count = 0
os.makedirs("../../Data/image/faceplusplus", exist_ok=True)
dataDump = open('../../Data/image/faceplusplus/DataDump.csv', 'w')
csvwriter = csv.writer(dataDump)
for link in links:
    if link[-3:] in ["jpg", "JPG", "png", "PNG"]:
        print(link)
        with open('../../Data/image/faceplusplus/apiKey', 'r') as myfile:
            apiKey = myfile.read().replace('\n', '')
        with open('../../Data/image/faceplusplus/apiSecret', 'r') as myfile:
            apiSecret = myfile.read().replace('\n', '')
        analyze_url = "https://api-us.faceplusplus.com/facepp/v3/detect"
        params     = {'api_key': apiKey, 'api_secret': apiSecret, 'image_url': link, 'return_attributes': 'gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,eyestatus,skinstatus'}
        getData(analyze_url, params, ids, count, csvwriter)
        count += 1
dataDump.close()

