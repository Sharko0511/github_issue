# dashboard.py
import plotly.graph_objs as go
import pandas as pd
from get_issue import get_issues  # Import get_issues directly from get_issue.py
from get_commit import get_commits  # Import get_commits directly from get_commit.py
from process_data import process_data  # Import process_data directly from process_data.py

# Fetch issues and commits from GitHub
issues = get_issues()
commits = get_commits()

# Process the fetched data to combine issues with commit details
processed_issues = process_data(issues, commits)

# Convert processed data to a DataFrame for easier manipulation
df = pd.DataFrame(processed_issues)

# Create a bar chart for LOC added and deleted per issue
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['title'],
    y=df['loc_added'],
    name='Lines Added',
    marker_color='green'
))

fig.add_trace(go.Bar(
    x=df['title'],
    y=df['loc_deleted'],
    name='Lines Deleted',
    marker_color='red'
))

fig.update_layout(
    title='Lines of Code Added and Deleted per Issue',
    xaxis_title='Issues',
    yaxis_title='Lines of Code',
    barmode='group'
)

# Show the dashboard (interactive plot in Jupyter Notebook or standalone HTML)
fig.show()