from teams import *

def check_players_number(team):
    if len(team) != 11:
        return False
    return True

def print_tactic(team):
    if check_players_number(team) == False:
        print("Numero di giocatori non corretto")
        return False

# dobbiamo trovare il migliore in campo della squadra, stampare il suo nome e il suo voto
def mvp(team):
    best_score = 0
    best_player =  ""
    for player in team:
        if player["score"] > best_score:
            best_score = player["score"]
            best_player = player["name"]
    
    print(best_player, best_score)

mvp(atletico_mendozzi)

# dobbiamo creare una funzione che stampa il modulo tattico della squadra, es: 4-3-3, 5-3-2, etc
def tactic(team):
    difensori = 0
    centrocampisti = 0
    attaccanti = 0

    for player in team:
        if player["role"] == "difensore":
            difensori += 1
        elif player["role"] == "centrocampista":
            centrocampisti += 1
        elif player["role"] == "attaccante":
            attaccanti += 1

    print(f"{difensori}-{centrocampisti}-{attaccanti}")

tactic(atletico_mendozzi)

def avg(team):
    player_number = len(team)

    total_score = 0
    for player in team:
        total_score = total_score + int(player["score"])

    avg_score = total_score / player_number
    print(avg_score)

avg(atletico_mendozzi)

# prendiamo il solito atletico e creiamo una funzione che ci restituisce una lista con i nomi di tutti
# i giocatori che hanno preso più di 6
def best_players(team):
    juvemerda = []
    for player in team:
        if player["score"] > 6:
            juvemerda.append(player["name"])
    return juvemerda
          

print(best_players(atletico_mendozzi))
