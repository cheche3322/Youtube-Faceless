from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from config.config import YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, YOUTUBE_DEVELOPER_KEY

def upload_video(title, description, file_path):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_DEVELOPER_KEY)
    
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['shorts', 'YouTube'],
            'categoryId': '22'
        },
        'status': {
            'privacyStatus': 'public'
        }
    }

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = request.execute()
    return response

if __name__ == "__main__":
    upload_video("Sample Video Title", "This is a sample video description.", "final_video.mp4")
