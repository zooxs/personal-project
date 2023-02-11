import json
from pprint import pprint
from glob import glob
from pandas import DataFrame, read_csv, merge

dir_files = './data/json_search'
dir_target = './data/results'

### open file resume.csv
df = read_csv(f"{dir_files}/resume_research.csv")

### open video's countries
with open(f"{dir_files}/countries.json", 'r') as countries:
    data_country = json.load(countries)

df_countries = DataFrame(data_country, index=['countries']).T.reset_index(level=0).rename(columns={'index':'channelId'})

### merge video's resume & video's countries at same channelId
df = merge(df, df_countries, on=['channelId', 'channelId'])

### open video's like counts file
with open(f"{dir_files}/likeCounts.json", 'r') as likeCounts:
    data_like = json.load(likeCounts)

data_like_count = dict()
for item in data_like.keys():
    vid = data_like[item]['items'][0]['id']
    stats = data_like[item]['items'][0]['statistics']# ['likeCount']
    data_like_count[vid] = stats

### merge previous merged data with video's like counts
df_stats = DataFrame(data_like_count).T.fillna('0').astype('int').reset_index(level=0).rename(columns={'index':'videoId'})

df = merge(df, df_stats[['videoId', 'likeCount']], on=['videoId', 'videoId'])

### open video's comments file
with open(f"{dir_files}/comments.json", 'r') as cm:
    data_comment = json.load(cm)

df_comment = DataFrame(data_comment).T.reset_index(level=0).rename(columns={'index':'videoId'})

### define a function to parse list of comment from its source
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

### apply previous function
df_comment['topLevelComment'] = df_comment.iloc[:, 4:5].apply(parse_comment, axis=1)
df_comment = df_comment.iloc[:, [0,6]]

### merge previous merged DataFrame with video's comment DataFrame
df = merge(df, df_comment, on=['videoId', 'videoId'])

### save to csv files
df.to_csv(f"{dir_files}/result.csv", index=False)