# main.py
from get_issue import get_issues
from get_commit import get_commits
from process_data import process_data

def main():
    print("Fetching issues...")
    issues = get_issues()
    print(f"Fetched {len(issues)} issues.")

    print("Fetching commits...")
    commits = get_commits()
    print(f"Fetched {len(commits)} commits.")

    combined_data = process_data(issues, commits)
    
    # Print information for each issue
    for issue in combined_data:
        state = issue.get('state', 'Unknown')  # Get the state of the issue (open or closed)
        
        print(f"Issue #{issue.get('number')}: {issue.get('title')}")
        print(f"  Created at: {issue.get('created_at')}")
        print(f"  State: {state}")  # Print whether the issue is open or closed
        print(f"  LOC Added: {issue.get('loc_added', 0)}")
        print(f"  LOC Deleted: {issue.get('loc_deleted', 0)}")
        print(f"  LOC to Solve: {issue.get('loc_to_solve', 0)}")
        print(f"  Commits: {issue.get('commits', [])}")
        print()  # Add a blank line for better readability

if __name__ == "__main__":
    main()


