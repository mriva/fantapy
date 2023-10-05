teams = ['Atletico Mendozzi', 'Virtus Secchi']

def ask_score(team_index):
    team_name = teams[team_index]
    score = input(f"Inserisci il punteggio ottenuto da {team_name}: ")
    return int(score)

def score_to_goals(score):
    if score >= 90:
        return 5
    elif score >= 84:
        return 4
    elif score >= 78:
        return 3
    elif score >= 72:
        return 2
    elif score >= 66:
        return 1

    return 0


team_0_score = ask_score(0)
team_1_score = ask_score(1)

team_0_goals = score_to_goals(team_0_score)
team_1_goals = score_to_goals(team_1_score)

results = {
    teams[0]: team_0_goals,
    teams[1]: team_1_goals,
}

print(results)
