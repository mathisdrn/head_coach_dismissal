import pandas as pd

match_results = pd.read_csv('data/match_results.csv', parse_dates=['date'])
head_coach = pd.read_csv('data/head_coach.csv', parse_dates=['appointed', 'end_date'])

unique_teams = list(set(match_results['home'].values.tolist() + match_results['away'].values.tolist()))
unique_teams_coach_change  = head_coach['team_name'].unique().tolist()

# Create dict team : league
team_league = {}
for team in unique_teams:
    team_league[team] = match_results[match_results['home'] == team]['league'].values[0]

league_team = {}
for league in match_results['league'].unique():
    league_team[league] = match_results[match_results['league'] == league]['home'].unique().tolist()

def filter_team(team_name, match_result = match_results):
    """For a given team it returns the following dataframe :
    - index : date
    - columns : goals, opponent_goals, opponent, away (boolean), result (win, draw, lose)"""
    df = match_result.copy()
    # Case 1: team is home
    home_team = df[df['home'] == team_name].copy()
    home_team['opponent'] = home_team['away']
    home_team['goals'] = home_team['home_goals']
    home_team['opponent_goals'] = home_team['away_goals']
    home_team['away'] = False
    home_team['result'] = home_team.apply(
        lambda x: 'win' if x['home_goals'] > x['away_goals']
        else 'draw' if x['home_goals'] == x['away_goals']
        else 'lose', axis=1)

    # Case 2 : team is away
    away_team = df[df['away'] == team_name].copy()
    away_team['opponent'] = away_team['home']
    away_team['goals'] = away_team['away_goals']
    away_team['opponent_goals'] = away_team['home_goals']
    away_team['away'] = True
    away_team['result'] = away_team.apply(
        lambda x: 'win' if x['away_goals'] > x['home_goals']
        else 'draw' if x['away_goals'] == x['home_goals']
        else 'lose', axis=1)
    
    # Concatenating both dataframes
    team_results = pd.concat([home_team, away_team], axis=0)
    columns_to_drop = ['home', 'home_goals', 'away_goals', 'total_goals']
    team_results = team_results.drop(columns=columns_to_drop, errors = 'ignore')
    team_results.set_index('date', inplace=True)
    team_results.sort_index(inplace=True)
    
    return team_results

