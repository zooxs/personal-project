from googleapiclient.discovery import build
import io
import json
# DEVELOPER_KEY = 'AIzaSyCHPNzLL2kPnc26D6XaAso6phBTJClMm1E'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
api_key_1 = 'AIzaSyCHPNzLL2kPnc26D6XaAso6phBTJClMm1E'
api_key_2 = 'AIzaSyC9HB5ANIoIXV9q-7R3xEWKUzdBoTwDlOA'
def youtube_build():
    DEVELOPER_KEY = api_key_1
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
    return youtube

def get_videos(keys, pageToken,numResults=50):
    youtube = youtube_build()
    request = youtube.search().list(
        part="snippet,id",
        q=keys, 
        pageToken=pageToken,
        type="video",
        maxResults = numResults
    )
    response = request.execute()
    return response

def get_video_country(channelID):
    request = youtube_build().channels().list(
        part="snippet",
        id=channelID
    )
    response = request.execute()
    return response

def get_like_counts(videoID):
    request = youtube_build().videos().list(
        part="statistics",
        id=videoID
    )
    response = request.execute()
    return response

def get_comments(videoID):
    request = youtube_build().commentThreads().list(
        part="snippet",
        videoId = videoID
    )
    response = request.execute()
    return response