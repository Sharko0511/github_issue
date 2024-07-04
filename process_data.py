# process_data.py
import re
from get_commit import get_loc_changes

def process_data(issues, commits):
    issue_commit_map = {}

    # Map commits to issues based on commit message references
    for commit in commits:
        commit_message = commit.get('commit', {}).get('message', '')
        commit_sha = commit.get('sha', '')
        loc_added, loc_deleted = get_loc_changes(commit_sha)
        
        # Look for issue references in commit message
        issue_numbers = re.findall(r'#(\d+)', commit_message)
        
        for issue_number in issue_numbers:
            if issue_number not in issue_commit_map:
                issue_commit_map[issue_number] = {'commits': [], 'loc_added': 0, 'loc_deleted': 0}
            
            issue_commit_map[issue_number]['commits'].append({'sha': commit_sha, 'loc_added': loc_added, 'loc_deleted': loc_deleted})
            issue_commit_map[issue_number]['loc_added'] += loc_added
            issue_commit_map[issue_number]['loc_deleted'] += loc_deleted

    # Calculate lines of code to solve per issue
    for issue in issues:
        issue_number = str(issue.get('number'))
        if issue_number in issue_commit_map:
            issue['commits'] = [commit['sha'] for commit in issue_commit_map[issue_number]['commits']]
            issue['loc_added'] = issue_commit_map[issue_number]['loc_added']
            issue['loc_deleted'] = issue_commit_map[issue_number]['loc_deleted']
            
            # Calculate lines of code needed to solve the issue
            loc_to_solve = sum(commit['loc_added'] - commit['loc_deleted'] for commit in issue_commit_map[issue_number]['commits'])
            issue['loc_to_solve'] = loc_to_solve
        else:
            issue['commits'] = [1,2,3]
            issue['loc_added'] = 3
            issue['loc_deleted'] = 4
            issue['loc_to_solve'] = 5

    return issues