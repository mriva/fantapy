altetico_medozzi_players = [
    {"name": "Maignan", "role": "portiere", "score": 8},
    {"name": "Theo", "role": "difensore", "score": 8},
    {"name": "Tomori", "role": "difensore", "score": 7},
    {"name": "Kjaer", "role": "difensore", "score": 6},
    {"name": "Calabria", "role": "difensore", "score": 6},
    {"name": "Reijnders", "role": "centrocampista", "score": 7},
    {"name": "Adli", "role": "centrocampista", "score": 7},
    {"name": "Loftus-Cheek", "role": "centrocampista", "score": 6},
    {"name": "Leao", "role": "attaccante", "score": 8},
    {"name": "Giroud", "role": "attaccante", "score": 10},
    {"name": "Pulisic", "role": "attaccante", "score": 7},
]

virtus_secchi_players = [
    {"name": "Provedel", "role": "portiere", "score": 6},
    {"name": "Hysaj", "role": "difensore", "score": 5},
    {"name": "Romagnoli", "role": "difensore", "score": 4},
    {"name": "Casale", "role": "difensore", "score": 5},
    {"name": "Marusic", "role": "difensore", "score": 5},
    {"name": "Luis Alberto", "role": "centrocampista", "score": 4},
    {"name": "Rovella", "role": "centrocampista", "score": 5},
    {"name": "Guendouzi", "role": "centrocampista", "score": 6},
    {"name": "Zaccagni", "role": "attaccante", "score": 5},
    {"name": "Castellanos", "role": "attaccante", "score": 6},
    {"name": "Felipe Anderson", "role": "attaccante", "score": 6},
]

teams_data = [
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

# def ask_score(team_index):
    # team_name = teams[team_index]
    # score = input(f"Inserisci il punteggio ottenuto da {team_name}: ")
    # return int(score)

def score_to_goals(score):
    if score < 60:
        return 0

    return (score - 60) // 6

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

    team_home_name = teams_data[0]["team_name"]
    team_away_name = teams_data[1]["team_name"]
    
    print(f"Il risultato è {team_home_name} - {team_away_name}: {team_0_goals} - {team_1_goals}")

    if team_0_goals > team_1_goals:
        mister_0 = teams_data[0]["mister"]
        print(f"Complimenti {mister_0}")
    elif team_1_goals > team_0_goals:
        mister_1 = teams_data[1]["mister"]
        print(f"Complimenti {mister_1}")
    else:
        print(f"Ha vinto lo sport")


def check_team(team):
    forward_number = 0

    for player in altetico_medozzi_players:
        if player["role"] == "attaccante":
            forward_number = forward_number + 1

    if forward_number > 3:
        print("La squadra non è valida")


team_0_score = 0
for player in altetico_medozzi_players:
    team_0_score = team_0_score + player["score"]

team_1_score = 0
for player in virtus_secchi_players:
    team_1_score = team_1_score + player["score"]

print_match_result(team_0_score, team_1_score)
