# dashboard.py
import plotly.graph_objs as go
import pandas as pd
from get_issue import get_issues
from get_commit import get_commits
from process_data import process_data

def main():
    # Fetch issues and commits from GitHub
    issues = get_issues()
    commits = get_commits()

    # Process the fetched data to combine issues with commit details
    processed_issues = process_data(issues, commits)

    # Convert processed data to a DataFrame for easier manipulation
    df = pd.DataFrame(processed_issues)

    # Create a bar chart for LOC added, deleted, and to solve per issue
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df['title'],
        y=df['loc_added'],
        name='Lines Added',
        marker_color='rgb(27, 207, 180)'
    ))

    fig.add_trace(go.Bar(
        x=df['title'],
        y=df['loc_deleted'],
        name='Lines Deleted',
        marker_color='rgb(254, 148, 150)'
    ))

    fig.add_trace(go.Bar(
        x=df['title'],
        y=df['loc_to_solve'],
        name='Lines to Solve',
        marker_color='rgb(75, 203, 235)'
    ))

    fig.update_layout(
        title='Lines of Code Added, Deleted, and to Solve per Issue',
        xaxis_title='Issues',
        yaxis_title='Lines of Code',
        barmode='group'
    )

    # Show the dashboard (interactive plot in Jupyter Notebook or standalone HTML)
    fig.show()

if __name__ == "__main__":
    main()
