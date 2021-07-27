import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('YOUTUBE_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername='schafer5'
)

response = request.execute()

print(response)
