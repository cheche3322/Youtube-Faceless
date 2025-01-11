from googleapiclient.discovery import build
from config.config import GOOGLE_ANALYTICS_API_KEY

def get_analytics(view_id, start_date, end_date):
    analytics = build('analyticsreporting', 'v4', developerKey=GOOGLE_ANALYTICS_API_KEY)
    response = analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
                    'metrics': [{'expression': 'ga:sessions'}]
                }
            ]
        }
    ).execute()
    return response

if __name__ == "__main__":
    view_id = "YOUR_VIEW_ID"
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    print(get_analytics(view_id, start_date, end_date))
