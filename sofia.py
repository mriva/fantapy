atletico_medozzi = [
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

virtus_secchi = [
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

virtus_secchi_cheat = [
    {"name": "Provedel", "role": "portiere", "score": 6},
    {"name": "Hysaj", "role": "difensore", "score": 5},
    {"name": "Romagnoli", "role": "difensore", "score": 4},
    {"name": "Casale", "role": "difensore", "score": 5},
    {"name": "Marusic", "role": "difensore", "score": 5},
    {"name": "Luis Alberto", "role": "centrocampista", "score": 4},
    {"name": "Rovella", "role": "centrocampista", "score": 5},
    {"name": "Ciro Immobile", "role": "attaccante", "score": 6},
    {"name": "Zaccagni", "role": "attaccante", "score": 5},
    {"name": "Castellanos", "role": "attaccante", "score": 6},
    {"name": "Felipe Anderson", "role": "attaccante", "score": 6},
]

virtus_secchi_coward = [
    {"name": "Provedel", "role": "portiere", "score": 6},
    {"name": "Hysaj", "role": "difensore", "score": 5},
    {"name": "Romagnoli", "role": "difensore", "score": 4},
    {"name": "Casale", "role": "difensore", "score": 5},
    {"name": "Marusic", "role": "difensore", "score": 5},
    {"name": "Pellegrini", "role": "difensore", "score": 5},
    {"name": "Luis Alberto", "role": "centrocampista", "score": 4},
    {"name": "Rovella", "role": "centrocampista", "score": 5},
    {"name": "Guendouzi", "role": "centrocampista", "score": 6},
    {"name": "Castellanos", "role": "attaccante", "score": 6},
    {"name": "Felipe Anderson", "role": "attaccante", "score": 6},
]

virtus_secchi_too_many = [
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
    {"name": "Ciro Immobile", "role": "attaccante", "score": 4},
]

""" Questa funzione deve prendere in input una delle squadre definite sopra
    e fare le seguenti cose:
        - controllare il numero di giocatori, se non è corretto stampare un messaggio di errore e ritornare False
        - controllare che giochi con il 4-3-3 (unica tattica accettata per ora), se non è corretto stampare un messaggio di errore e ritornare False
        - se entrambi i controlli precedenti sono corretti stampare un messaggio di congratulazioni per non aver barato e ritornare True

    Ah, una volta definita la funzione ricordatevi che va chiamata, altrimenti il programma non fa nulla

    Ho preparato delle squadre di esempio, alcune buone altre con errori, per testare la funzione
"""
def check_team_linueup(team):
    team_number = 0

    for player in team:
        team_number = team_number + 1 

    if team_number == 11:
        print ("complimenti!! sai quante persone ci sono in una squadra")
        return True
    else: 
        print ("bro, si gioca in 11") 
        return False

check_team_linueup(atletico_medozzi)

def check_tactics(team):
    forward_count = 0
    for player in team:
        if ["role"] == "attaccante":
            forward_count = forward_count + 1
        if ["role"] == "centrocampista":
            midfielder_count = midfielder_count + 1
            
    midfielder_count = 0
    for player in team:
         if ["role"] == "centrocampista":
            midfielder_count = midfielder_count + 1

    defender_count = 0 
    for player in team:
        if ["role"] == "difensore":
         defender_count = defender_count + 1

    if forward_count != 3: 
        print("il numero di attaccanti è sbagliato")
        return "false"

    elif midfielder_count != 3:
        print ("il numero di centrocampisti è sbagliato")
        return "false"
    
    elif defender_count !=4:
        print("il numero di difensori è sbagliato")
        return "false"

    else:
        print ("complimenti, la formazione è corretta")
        return "true"

check_tactics(virtus_secchi_cheat)
