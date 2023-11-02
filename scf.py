import random

scf = [
    "sasso",
    "carta",
    "forbice",
]

def ask_user():
    response = input("Sasso carta o forbice? ")
    if response in scf:
        return response
    else:
        print("fottiti")

def create_choice():
    random_number = random.randint(0, 2)
    choice = scf[random_number]
    print(choice)
    return choice

def winner(response, choice):
    if response == "sasso":
        if choice == "forbice":
            print ("hai vinto")
        if choice == "sasso":
            print ("pari")
        if choice == "carta":
            print ("Hai perso")

    if response == "forbice":
        if choice == "forbice":
            print ("pari")
        if choice == "sasso":
            print ("hai perso")
        if choice == "carta":
            print ("Hai vinto")

    if response == "carta":
        if choice == "forbice":
            print ("hai perso")
        if choice == "sasso":
            print ("hai vinto")
        if choice == "carta":
            print ("pari")

user_response = ask_user()
computer_choice = create_choice()
winner(user_response, computer_choice)