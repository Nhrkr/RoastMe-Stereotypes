import requests
import json
import os

with open('metadata.json') as f:
    data = json.load(f)

for item in data['data']['children']:
    link = item['data']['url']
    if link[-3:] == "jpg":
        print(link)
        with open('faceplusplus/apiKey', 'r') as myfile:
            apiKey = myfile.read().replace('\n', '')
        with open('faceplusplus/apiSecret', 'r') as myfile:
            apiSecret = myfile.read().replace('\n', '')
        analyze_url = "https://api-us.faceplusplus.com/facepp/v3/detect"
        params     = {'api_key': apiKey, 'api_secret': apiSecret, 'image_url': link, 'return_attributes': 'gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,eyestatus,skinstatus'}
        os.makedirs("faceplusplus", exist_ok=True)
        try:
            response = requests.post(analyze_url, params = params)
            response.raise_for_status()
            analysis = response.json()
            print(analysis)
            with open('faceplusplus/'+item['data']['id']+'.json', 'w') as outfile:
                json.dump(analysis, outfile)
        except requests.exceptions.HTTPError as e:
            print(e)


