import json
from pprint import pprint
from glob import glob
from pandas import DataFrame
dir_files = './data/json_search/'

ls_files = glob(f"{dir_files}*json")

resume_search = dict()

ls_videoId = []
ls_channelId = []
ls_title = []
ls_description = []
ls_publishAt = []
ls_videoUrl = []

for js_files in ls_files:

    with open(js_files, 'r') as f:
        data = json.load(f)

    for data_key in data.keys():
        for item in data[data_key]['items']:
            videoId = item['id']['videoId']
            videoUrl = f"https://www.youtube.com/watch?v={videoId}"
            channelId = item['snippet']['channelId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            publishAt = item['snippet']['publishedAt']
            ls_videoId.append(videoId)
            ls_channelId.append(channelId)
            ls_title.append(title)
            ls_description.append(description)
            ls_publishAt.append(publishAt)
            ls_videoUrl.append(videoUrl)

    resume_search['videoId'] = ls_videoId
    resume_search['channelId'] = ls_channelId
    resume_search['title'] = ls_title
    resume_search['description'] = ls_description
    resume_search['publishAt'] = ls_publishAt
    resume_search['videoUrl'] = ls_videoUrl


df = DataFrame(resume_search)
df.to_csv(f"{dir_files}resume_research.csv", index=False)
# print(df.shape)



