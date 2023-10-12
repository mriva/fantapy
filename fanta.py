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

# teams = [
#     "Atletico Mendozzi",
#     "Virtus Secchi",
# ]

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


# teams_data = {
#     "Atletico Mendozzi": "Sofia",
#     "Virtus Secchi": "Tommaso",
# }

def ask_score(team_index):
    team_name = teams[team_index]
    score = input(f"Inserisci il punteggio ottenuto da {team_name}: ")
    return int(score)

def score_to_goals_old(score):
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

def score_to_goals(score):
    if score < 60:
        return 0

    return (score - 60) // 6

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


# team_0_score = ask_score(0)
# team_1_score = ask_score(1)

# la funzione prende un team (cioè un dictionary) e controlla se ci sono troppi attaccanti
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
