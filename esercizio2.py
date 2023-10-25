from teams import *

def check_players_number(team):
    if len(team) != 11:
        return False
    return True

def print_tactic(team):
    if check_players_number(team) == False:
        print("Numero di giocatori non corretto")
        return False

def mvp(team):
    max = 0
    mvp = ""

    for players in team:
        if players["score"] > max:
            max = players["score"]
            mvp = players["name"]

    print(f"Il migliore in campo è stato {mvp} con il voto di {max}")

mvp(altetico_medozzi)

# list of n fibonacci values
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci(10))
