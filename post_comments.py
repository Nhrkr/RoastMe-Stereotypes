
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
comments_file='G:/Stereotypes/post_comments.csv'


with open(posts_file,'r', encoding='utf-8') as f:
    filereader = csv.reader(f)
    posts_list = list(filereader)

s=requests.session()

list_comments=list()
list_comments.append(('index', 
posts_list.pop(0)

for id in posts_list:
	
	print(id[1])
	url='https://www.reddit.com/r/roastme/comments/'+id[1]+'.json'
	response= s.get(url,headers = {'User-agent': 'Chrome'})
	data = json.loads(response.content.decode('utf-8'))[1]['data']['children']
	print(len(data))
	for i in range(len(data)):
		print(i)
		if data[i]['kind']=='t1':
			post_id=id[1]
			comment_id=data[i]['data']['id']
			comment_name=data[i]['data']['name']
			comment_title=data[i]['data']['body']
			comment_author=data[i]['data']['author']
			comment_url=data[i]['data']['permalink']
			comment_created=data[i]['data']['created']
			comment_ups=data[i]['data']['ups']
			comment_score=data[i]['data']['score']
			comment_is_submitter=data[i]['data']['is_submitter']
			tuple_var = (i,post_id,comment_id,comment_name,comment_title,comment_author,comment_url, comment_created, comment_ups,comment_score,comment_is_submitter)
			list_comments.append(tuple_var)
	break	
print(len(list_comments))
writeCsvFile(comments_file, list_comments)
