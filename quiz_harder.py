questions = [
    {
        "question": "Che cosa è un autoveicolo?",
        "answers": [
            { "text": "Un mezzo semovente a pedali di almeno 3,5 tonnellate", "correct": False },
            { "text": "Qualsiasi veicolo a motore proprio, con almeno quattro ruote, atto a circolare su strada ordinaria indipendentemente da impianti fissi", "correct": True },
            { "text": "Un veicolo composto da due motocicli saldati insieme", "correct": False },
            { "text": "Una carrozza trainata da uno o più cavalli", "correct": False }
        ]
    },
    {
        "question": "Come è fatto il segnale di diveto di sosta?",
        "answers": [
            { "text": "Un ottagono blu", "correct": False },
            { "text": "Un triangolo verde", "correct": False },
            { "text": "Un dodecagono fucsia", "correct": False },
            { "text": "Un cerchio blu con delle cose rosse", "correct": True }
        ]
    },
    {
        "question": "Qual è il limite di velocità nei centri urbani?",
        "answers": [
            { "text": "100 km/h", "correct": False },
            { "text": "200 km/h", "correct": False },
            { "text": "Non c'è un limite, dipende da quanta fretta hai", "correct": True },
            { "text": "300 km/h", "correct": False },
        ]
    },
    {
        "question": "A cosa serve il clacson?",
        "answers": [
            { "text": "A segnalare chi sta davanti che deve muoversi", "correct": True },
            { "text": "A disperdere i gabbiani", "correct": False },
            { "text": "Ad avvertire di un imminente pericolo", "correct": False },
            { "text": "A salutare la gente per strada se vivi al sud", "correct": False },
        ]
    }
]


def print_question(question_to_print):
    print(question_to_print["question"])


def print_answers(question_to_print):
    for i, answer in enumerate(question_to_print["answers"]):
        print(f"{i + 1}: {answer['text']}")

def get_correct_answer(answers):
    index = 0
    for answer in answers:
        index += 1
        if answer["correct"] == True:
            return str(index)

correct_answers = 0
for question in questions:
    print_question(question)
    print_answers(question)

    response = input("Inserisci la tua risposta: ")
    if response == get_correct_answer(question["answers"]):
        correct_answers += 1

print(f"Hai ottenuto {correct_answers} risposte corrette e {4 - correct_answers} risposte sbagliate")


