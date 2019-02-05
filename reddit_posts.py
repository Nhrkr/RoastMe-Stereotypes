# -*- coding: utf-8 -*-
"""
Created on Thu 1/31/2019

@author: Niharika
"""

# -*- coding: utf-8 -*-

import csv
import requests
import json
import sys

def writeCsvFile(fname, data):
 
    mycsv = csv.writer(open(fname, 'w', encoding='utf-8',newline=''))
    for row in data:
        mycsv.writerow(row)

posts_file='G:/Stereotypes/top_posts.csv'

s=requests.session()

list_posts=list()
list_posts.append(('index','id','name','title','author','url','created','ups','score','num_comments'))

for j in range(3):
	if j ==0:
		api='https://www.reddit.com/r/Roastme/top.json?limit=100&sr_detail&show=all'
		print(api)
	else:
		api='https://www.reddit.com/r/Roastme/top.json?limit=100&sr_detail&show=all&after='+next
		print(api)
	response= s.get(api,headers = {'User-agent': 'Chrome'})

	data = json.loads(response.content.decode('utf-8'))['data']['children']
	print(len(data))
	next = data[len(data)-1]['data']['name']
	counter=0
	for i in range(len(data)):
		post_id=data[i]['data']['id']
		post_name=data[i]['data']['name']
		post_title=data[i]['data']['title']
		post_author=data[i]['data']['author']
		# post_author_fullname=data[i]['data']['author_fullname']
		post_url=data[i]['data']['url']
		post_created=data[i]['data']['created']
		post_ups=data[i]['data']['ups']
		post_score=data[i]['data']['score']
		post_num_comments=data[i]['data']['num_comments']
		tuple_var = ((i+10*j),post_id,post_name,post_title,post_author,post_url, post_created, post_ups,post_score,post_num_comments)
		list_posts.append(tuple_var)
	print(next)		
print(len(list_posts))
writeCsvFile(posts_file, list_posts)

