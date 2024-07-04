# get_commit.py
import requests
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
commits_url = f'https://api.github.com/repos/{owner}/{repo}/commits'

# Headers with the GitHub token for authentication
headers = {
    'Authorization': f'token {token}'
}

def get_commits():
    params = {}
    response_commits = requests.get(commits_url, headers=headers, params=params)

    if response_commits.status_code == 200:
        return response_commits.json()
    else:
        print(f"Failed to fetch commits: {response_commits.status_code}")
        print(response_commits.text)
        return []

def get_loc_changes(commit_sha):
    commit_details_url = f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}'
    response_commit_details = requests.get(commit_details_url, headers=headers)
    if response_commit_details.status_code == 200:
        commit_details = response_commit_details.json()
        files = commit_details.get('files', [])
        loc_added = sum(file.get('additions', 0) for file in files)
        loc_deleted = sum(file.get('deletions', 0) for file in files)
        return loc_added, loc_deleted
    else:
        print(f"Failed to fetch commit details: {response_commit_details.status_code}")
        print(response_commit_details.text)
        return 0, 0
