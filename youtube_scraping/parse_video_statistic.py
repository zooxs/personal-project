import json
from pprint import pprint
from glob import glob
from pandas import DataFrame, read_csv, merge
dir_files = './data/json_search/'

df = read_csv(f"{dir_files}resume_research.csv")

with open(f"{dir_files}countries.json", 'r') as countries:
    data_country = json.load(countries)

df_countries = DataFrame(data_country, index=['countries']).T.reset_index(level=0).rename(columns={'index':'channelId'})

df = merge(df, df_countries, on=['channelId', 'channelId'])

with open(f"{dir_files}likeCounts.json", 'r') as likeCounts:
    data_like = json.load(likeCounts)

data_like_count = dict()
for item in data_like.keys():
    vid = data_like[item]['items'][0]['id']
    stats = data_like[item]['items'][0]['statistics']# ['likeCount']
    data_like_count[vid] = stats

df_stats = DataFrame(data_like_count).T.fillna('0').astype('int').reset_index(level=0).rename(columns={'index':'videoId'})

df = merge(df, df_stats[['videoId', 'likeCount']], on=['videoId', 'videoId'])

with open(f"{dir_files}comments.json", 'r') as cm:
    data_comment = json.load(cm)

df_comment = DataFrame(data_comment).T.reset_index(level=0).rename(columns={'index':'videoId'})
def parse_comment(ls):
    if ls.values != 'Comments Disabled':
        length_comment = len(ls.values[0])
        
        if length_comment < 3:
            
            ls_topLevelComment = []
            for i in ls.values[0]:
                topComment = i['snippet']['topLevelComment']['snippet']['textDisplay']
                ls_topLevelComment.append(topComment)
            return ls_topLevelComment
        else:
            
            ls_topLevelComment = []
            for i in ls.values[0][:3]:
                topComment = i['snippet']['topLevelComment']['snippet']['textDisplay']
                ls_topLevelComment.append(topComment)
            return ls_topLevelComment
    else: return ['There is no comments']

df_comment['topLevelComment'] = df_comment.iloc[:, 4:5].apply(parse_comment, axis=1)
df_comment = df_comment.iloc[:, [0,6]]

df = merge(df, df_comment, on=['videoId', 'videoId'])

df.to_csv(f"{dir_files}result.csv", index=False)