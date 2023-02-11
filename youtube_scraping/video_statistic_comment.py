from pandas import read_csv
from ytscrapper.ytmethod import *
from pprint import pprint
filepath = './data/results/resume_research.csv'

df = read_csv(filepath)
ls_videoId = df['videoId'].to_list()
ls_channelId = df['channelId'].to_list()

tes_vId = ls_videoId[9]
tes_cId = ls_channelId[0]

likeCounts = dict()
ls_comments = dict()

### get video's statistics & top comments
for idx, videoId in enumerate(ls_videoId):
    video_req = get_like_counts(videoId)
    likeCounts[f'iter_{idx}'] = video_req
    comment_req = get_comments(videoId)
    comments[f'iter_{idx}'] = comment_req
    print(f'iteration ---- {idx}')

with open('./data/json_search/likeCounts.json', 'w') as like_counts:
    json.dump(likeCounts, like_counts)


for idx, videoId in enumerate(ls_videoId):
    try:
        commentsThread = get_comments(videoId)
        ls_comments[f'{videoId}'] = commentsThread
    except:
        ls_comments[f'{videoId}'] = 'Comments Disabled'
    print(f'iteration ---- {idx}')

with open('./data/json_search/comments.json', 'w') as file_comment:
    json.dump(ls_comments, file_comment)

### get video's country
ls_country = dict()
for idc, channel in enumerate(ls_channelId):
    for item in get_video_country(channel)['items']:
        if 'country' not in item['snippet'].keys():
            ls_country[f'{channel}'] = '--'
        else:
            ls_country[f'{channel}'] = item['snippet']['country']
        print(f'iteration ---- {idc}')
            
with open('./data/json_search/countries.json', 'w') as file_country:
    json.dump(ls_country, file_country)