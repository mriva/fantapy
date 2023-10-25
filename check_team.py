from teams import *

""" Questa funzione deve prendere in input una delle squadre definite sopra
    e fare le seguenti cose:
        - controllare il numero di giocatori, se non è corretto stampare un messaggio di errore e ritornare False
        - controllare che giochi con il 4-3-3 (unica tattica accettata per ora), se non è corretto stampare un messaggio di errore e ritornare False
        - se entrambi i controlli precedenti sono corretti stampare un messaggio di congratulazioni per non aver barato e ritornare True

    Ah, una volta definita la funzione ricordatevi che va chiamata, altrimenti il programma non fa nulla

    Ho preparato delle squadre di esempio, alcune buone altre con errori, per testare la funzione
"""
def check_team_linueup(team):
    if len(team) != 11:
        print("Numero di giocatori non corretto")
        return False

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

    if difensori != 4 or centrocampisti != 3 or attaccanti != 3:
        print("Tattica non corretta")
        return False

    print("Congratulazioni, non hai barato")


print("Controllo Atletico Medozzi")
check_team_linueup(altetico_medozzi)
print()

print("Controllo Virtus Secchi")
check_team_linueup(virtus_secchi)
print()

print("Controllo Virtus Secchi Cheat")
check_team_linueup(virtus_secchi_cheat)
print()

print("Controllo Virtus Secchi Coward")
check_team_linueup(virtus_secchi_coward)
print()

print("Controllo Virtus Secchi Too Many")
check_team_linueup(virtus_secchi_too_many)

