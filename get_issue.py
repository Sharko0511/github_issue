# get_issue.py
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the GitHub token from the environment variable
token = os.getenv('GITHUB_TOKEN')

# GitHub repository details
owner = 'Sharko0511'
repo = 'discord-clone'

# GitHub API endpoint
issues_url = f'https://api.github.com/repos/{owner}/{repo}/issues'

# Headers with the GitHub token for authentication
headers = {
    'Authorization': f'token {token}'
}

def get_issues():
    # Fetch both open and closed issues from the last week
    last_week = datetime.now() - timedelta(days=7)
    params = {
        'since': last_week.isoformat(),
        'state': 'all'  # Include both open and closed issues
    }

    response = requests.get(issues_url, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch issues: {response.status_code}")
        print(response.text)
        return []

