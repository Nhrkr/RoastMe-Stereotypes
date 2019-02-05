import requests
import json
import os

with open('metadata.json') as f:
    data = json.load(f)

for item in data['data']['children']:
    link = item['data']['url']
    if link[-3:] == "jpg":
        print(link)
        analyze_url = "https://api-us.faceplusplus.com/facepp/v3/detect"
        params     = {'api_key': 'PwLFuJOmO0Z4rSAJlEq2JvQ5xlfPDb5r', 'api_secret': 'eRLnFwZbbxGD-l0BKe5LK3pV86pQSdH7', 'image_url': link, 'return_attributes': 'gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,eyestatus,skinstatus'}
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


