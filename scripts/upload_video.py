from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from config.config import YOUTUBE_API_KEY

def upload_video(title, description, file_path):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request_body = {
        'snippet': {
            'title': title,
            'description': description
        },
        'status': {
            'privacyStatus': 'public'
        }
    }
    media = MediaFileUpload(file_path)
    response = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media
    ).execute()
    return response

if __name__ == "__main__":
    title = "Sample Video"
    description = "This is a sample video uploaded using YouTube Data API."
    file_path = "static/thumbnails/final_video.mp4"
    print(upload_video(title, description, file_path))
