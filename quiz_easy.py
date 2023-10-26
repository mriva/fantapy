# In questo esercizio creeremo un simulatore di quiz per la patente
# 
# la prima cosa che dovete fare è: data la domanda scritta sotto, scrivere il codice che esegue queste operazioni:
# - stampa la domanda
# - stampa le risposte con un indice numerico prima del testo (i numeri devono partire da 1)
# - chiede all'utente di inserire il numero della risposta corretta
# - stampa "Risposta corretta" se l'utente ha indovinato, "Risposta sbagliata" altrimenti
#
# se questo esercizio vi risulta facile, mandatemi la soluzione e vi propongo la seconda versione più hard

question = {
    "question": "Che cosa è un autoveicolo?",
    "answers": [
        { "text": "Un mezzo semovente a pedali di almeno 3,5 tonnellate", "correct": False },
        { "text": "Qualsiasi veicolo a motore proprio, con almeno quattro ruote, atto a circolare su strada ordinaria indipendentemente da impianti fissi", "correct": True },
        { "text": "Un veicolo composto da due motocicli saldati insieme", "correct": False },
        { "text": "Una carrozza trainata da uno o più cavalli", "correct": False }
    ]
}

print(question["question"])
number = 0
for answer in question["answers"]:
    number = number + 1
    print(str(number) + ". " + answer["text"])

input = input("Scegli la risposta corretta: ")

correct_answer = 0

index = 0
for answer in question["answers"]:
    index += 1
    if answer["correct"] == True:
        correct_answer = str(index)

if input == correct_answer:
    print("Complimenti, risposta esatta")
else:
    print("Sei stato bocciato")
