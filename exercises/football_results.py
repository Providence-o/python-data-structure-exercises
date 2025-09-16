# This file contains a list of results from Group F of the Euro 2016
# championship.  Each item in the list of results is a dictionary, whose keys
# are the names of the teams playing a match, and whose values are the number
# of goals scored by each team in the match.
#
# When the file is run, it should display some facts about the final results in
# the group.
#
# NB Teams score three points for a win and one point for a draw.

results = [
        {'Austria': 0, 'Hungary': 2},
        {'Portugal': 1, 'Iceland': 1},
        {'Iceland': 1, 'Hungary': 1},
        {'Portugal': 0, 'Austria': 0},
        {'Iceland': 2, 'Austria': 1},
        {'Hungary': 3, 'Portugal': 3},
]

print('There were {} matches in the group'.format(len(results))) 



# print('The match with the most goals was', '?')
# print('The match with the fewest goals was', '?')
# print('The team with the most total goals was', '?')
# print('The team with the fewest total goals was', '?')
# print('The team with the most points was', '?')
# print('The team with the fewest points was', '?')



# TODO: Write code to answer the following questions:
# write code to compute number of goals per match 
def calculate_match_goal():
    match_result = {}
    for match in results: 
        (team_1, score_1), (team_2, score_2) = match.items() # dict_items convert the key-value pairs to tuples 
        match_name = f'{team_1}-{team_2}'
        match_result[match_name] = score_1 + score_2

    max_match_goals = max(match_result, key=match_result.get)
    min_match_goals = min(match_result, key=match_result.get)

    return f'The match with the most goals was? \n{max_match_goals} \nThe match with the fewest goals was? \n{min_match_goals}'
print(calculate_match_goal())
     
    

# write code to compute number of goals per team

# first get the list of teams 
def team_names():
    team_list = set()
    for match in results:
        team_list.update(match.keys())
    return team_list

# second, iterate through the list of team names and call get() to extract corresponding values
def goal_per_team():
    teams = team_names()

    team_dict = {}  
    for t in teams:
        score = 0 
        for match in results:
            if t in match:
                score += match[t]
                team_dict[t] = score

    max_team_goals = max(team_dict, key=team_dict.get)
    min_team_goals = min(team_dict, key=team_dict.get)

    max_goal = team_dict.get(max_team_goals)
    min_goal = team_dict.get(min_team_goals)
    return f'The team with the most total goals was? \n{max_team_goals}: {max_goal} goals \nThe team with the fewest total goals was? \n{min_team_goals}: {min_goal} goals'
    
print(goal_per_team())


# write function to calculate the number of points per match per team 
def match_points_per_team():
    team_points = {}
    teams = team_names()
    for t in teams:
        points = 0
        for match in results: 
            (team_1, score_1), (team_2, score_2) = match.items()
            if t == team_1 and score_1 > score_2:
                points += 3
            elif t == team_2 and score_2 > score_1:
                points += 3
            elif score_1 == score_2 and (t == team_1 or t == team_2):
                points += 1
        team_points[t] = points
    max_team_points = max(team_points, key=team_points.get)
    min_team_points = min(team_points, key=team_points.get)

    max_point = team_points.get(max_team_points)
    min_point = team_points.get(min_team_points)
    return f'The team with the most points was? \n{max_team_points}: {max_point} points \nThe team with the fewest points was? \n{min_team_points}: {min_point} points'

print(match_points_per_team())




# TODO (extra): Write code to compute and display a league table

