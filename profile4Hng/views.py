from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
GITHUB_FILE_URL = "https://github.com/Pundits-iTech/HNG_Stage_One_Task/blob/main/twoParametersApi/profile4Hng/views.py"
GITHUB_REPO_URL = "https://github.com/Pundits-iTech/HNG_Stage_One_Task"

class SlackFirstTask(APIView):
    def get(self, request):
        # Get the current date and time
        current_datetime = datetime.now()
        # Get the current UTC time
        current_utc_time = datetime.now(pytz.utc)

        # Format the UTC time in the desired format
        formatted_utc_time = current_utc_time.strftime(DATE_FORMAT)
        # For example, if you want to convert it to New York time:
        accra_timezone = pytz.timezone('Africa/Accra')
        current_accra_time = current_utc_time.astimezone(accra_timezone)
        # Get the day of the week as an integer (0 for Monday, 1 for Tuesday, etc.)
        day_of_week = current_accra_time.weekday()

        # You can convert it to a string if needed
        day_name = current_accra_time.strftime('%A')

        slack_name = request.GET.get("slack_name", "Mohammed Ali")
        track = request.GET.get("track", "Backend")
        if not slack_name:
            return Response({"message": "slack_name must not be empty"}, status=status.HTTP_400_BAD_REQUEST)
        if not track:
            return Response({"message": "track must not be empty"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            "slack_name": slack_name,
            "current_day": day_name,
            "utc_time": formatted_utc_time,
            "track": track,
            "github_file_url": GITHUB_FILE_URL,
            "github_repo_url": GITHUB_REPO_URL,
            "status_code": status.HTTP_200_OK
        }
        return Response(data, status=status.HTTP_200_OK)
