# process_data.py
import re
from get_commit import get_loc_changes

def process_data(issues, commits):
    issue_commit_map = {}

    for commit in commits:
        commit_message = commit.get('commit', {}).get('message', '')
        commit_sha = commit.get('sha', '')
        loc_added, loc_deleted = get_loc_changes(commit_sha)
        
        # Look for issue references in commit message
        issue_numbers = re.findall(r'#(\d+)', commit_message)
        
        for issue_number in issue_numbers:
            if issue_number not in issue_commit_map:
                issue_commit_map[issue_number] = {'commits': [], 'loc_added': 0, 'loc_deleted': 0, 'loc_to_solve': 0}
            
            issue_commit_map[issue_number]['commits'].append(commit_sha)
            issue_commit_map[issue_number]['loc_added'] += loc_added
            issue_commit_map[issue_number]['loc_deleted'] += loc_deleted

    # Now, calculate lines of code to solve per issue
    for issue in issues:
        issue_number = str(issue.get('number'))
        if issue_number in issue_commit_map:
            issue['commits'] = issue_commit_map[issue_number]['commits']
            issue['loc_added'] = issue_commit_map[issue_number]['loc_added']
            issue['loc_deleted'] = issue_commit_map[issue_number]['loc_deleted']
            
            # Calculate lines of code needed to solve the issue
            loc_to_solve = sum(commit.get('loc_added', 0) - commit.get('loc_deleted', 0) for commit in issue_commit_map[issue_number]['commits'])
            issue['loc_to_solve'] = loc_to_solve

    return issues
