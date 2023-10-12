teams = [
    "Atletico Mendozzi",
    "Virtus Secchi",
]

teams_improved_version = [
    {
        "team_name": "Atletico Mendozzi",
        "mister": "Sofia",
        "sponsor": "Mapei"
    },
    {
        "team_name": "Virtus Secchi",
        "mister": "Tommaso",
        "sponsor": "Adidas"
    }
]

teams_data = {
    "Atletico Mendozzi": "Sofia",
    "Virtus Secchi": "Tommaso",
}

print(teams[0])
print(teams_improved_version[0]["team_name"])

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

# vogliamo una funzione che prende in input i due score, e ci stampa questo:
# Il risultato è Squadra_a 1 - Squadra_b 0    
def print_match_result(team_0_score, team_1_score):
    team_0_goals = score_to_goals(team_0_score)
    team_1_goals = score_to_goals(team_1_score)

    if team_0_goals == team_1_goals:
        if abs(team_0_score - team_1_score) >= 4:
            if team_0_score > team_1_score:
                team_0_goals = team_0_goals + 1
            else:
                team_1_goals = team_1_goals + 1
    if abs(team_0_score - team_1_score) >= 10:
        if team_0_score > team_1_score:
            team_0_goals = team_0_goals + 1 
        else:
            team_1_goals = team_1_goals + 1

    print(f"Il risultato è {teams[0]} - {teams[1]}: {team_0_goals} - {team_1_goals}")

    if team_0_goals > team_1_goals:
        mister_0 = teams_data[teams[0]]
        print(f"Complimenti {mister_0}")
    elif team_1_goals > team_0_goals:
        mister_1 = teams_data[teams[1]]
        print(f"Complimenti {mister_1}")
    else:
        print(f"Ha vinto lo sport")


team_0_score = ask_score(0)
team_1_score = ask_score(1)

print_match_result(team_0_score, team_1_score)
