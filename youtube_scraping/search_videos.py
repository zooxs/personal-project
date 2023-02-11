from ytscrapper.ytmethod import *
# , thinspiration, fitspiration, body image
key = "mukbang, nutrition, ASMR"
# key = "thinspiration, fitspiration, body image"

"""
search videos based on keywords,
get list of all information
"""
dir_target = './data/json_search/'
pageToken = 'CKYEEAE'
num_iter = 0
json_files = dict()
while True:
    result = get_videos(key, pageToken)
    json_files[f'iter_{num_iter}'] = result
    print(f'iteration ----- {num_iter}')
    if 'nextPageToken' not in result.keys():
        break
    else:
        pageToken = result['nextPageToken']
        num_iter += 1
    if num_iter == 7:
        break


with open(f"{dir_target}search5.json", "w") as f:
    json.dump(json_files, f)