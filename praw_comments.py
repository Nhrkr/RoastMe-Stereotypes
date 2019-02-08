from os.path import isfile
import praw
import pandas as pd
from time import sleep
from praw.models import MoreComments
# Get credentials from DEFAULT instance in praw.ini
reddit = praw.Reddit()

def get_post_comment(id,df,csv):
  sub_dict = {'id': [],'body': [] , 'author': [],'is_submitter': [], 'permalink': [], 'score': []}
  submission = reddit.submission(id=id)
  
  for top_level_comment in submission.comments.replace_more(limit=None):
    # unique_id = top_level_comment.id not in tuple(df.id) if csv_loaded else True
    # Save any unique top_level_comments to sub_dict.
    # if unique_id:
    sub_dict['id'].append(top_level_comment.id)
    sub_dict['body'].append(top_level_comment.body)
    sub_dict['author'].append(top_level_comment.author)
    sub_dict['is_submitter'].append(top_level_comment.is_submitter)
    sub_dict['permalink'].append(top_level_comment.permalink)
    sub_dict['score'].append(top_level_comment.score)
  new_df = pd.DataFrame(sub_dict)
  if 'DataFrame' in str(type(df)):
    pd.concat([df, new_df], axis=0, sort=0).to_csv(csv, index=False)
    print(f'{len(new_df)} new posts collected and added to {csv}')
  else:
    new_df.to_csv(csv, index=False)
    print(f'{len(new_df)} posts collected and saved to {csv}')
  print(len(new_df))    
  return new_df

def all_comments(csv_post_id, csv_comment):
  post_df, csv_loaded = (pd.read_csv(csv_post_id), 1) if isfile(csv_post_id) else ('', 0)
  comment_df, csv_loaded = (pd.read_csv(csv_comment), 1) if isfile(csv_comment) else ('', 0)
  for i in post_df['id']:
    print('Getting comments for id '+ i)
    comment_df=get_post_comment(i,comment_df,csv_comment)
  return None

all_comments('roastme_posts.csv','roastme_comments.csv')
