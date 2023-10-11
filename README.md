# This is a simple Api developed using django-rest framework.
The endpoint takes two GET request query parameters and return specific information in JSON format.
FORMAT OF THE JSON FILE: 

JSON

    {
      "slack_name": "example_name",
      
      "current_day": "Monday",
      
      "utc_time": "2023-08-21T15:04:05Z",
      
      "track": "backend",
      
      "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
      
      "github_repo_url": "https://github.com/username/repo",
      
      “status_code”: 200
    }
