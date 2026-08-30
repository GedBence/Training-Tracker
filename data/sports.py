# ------------------------------------------
# TÁMOGATOTT SPORTÁGAK
# ------------------------------------------

SPORTS = {
    "1": "Muay Thai",
    "2": "Box",
    "3": "Futás",
    "4": "Úszás",
    "5": "Erősítő edzés",
    "6": "Kerékpározás",
    "7": "Egyéb"
}

SPORT_QUESTIONS = {
    "Muay Thai": [
        {"key": "sparring", "question": "Volt sparring? (i/n): ", "type": str},
        {"key": "menetek", "question": "Menetek száma: ", "type": int},
    ],
    "Box": [
        {"key": "menetek", "question": "Menetek száma:", "type": int},
        {"key": "ko", "question": "Ko száma: ", "type": int},
    ],
    "Futás": [
        {"key": "tavolsag_km", "question": "Táv (km): ", "type": float},
        {"key": "tempo", "question": "Átlagtempó (perc/km): ", "type": str},
    ],
    "Úszás": [
        {"key": "tavolsag_m", "question": "Táv (m): ", "type": int},
        {"key": "stilus", "question": "Stílus: ", "type": str},
    ],
    "Erősítő edzés": [
        {"key": "izomcsoport", "question": "Fő izomcsoport: ", "type": str},
        {"key": "szettek", "question": "Szettek száma: ", "type": int},
    ],
    "Kerékpározás": [
        {"key": "tavolsag_km", "question": "Táv (km)", "type": float},
        {"key": "atlagseg_kmh", "question": "Átlagsebesség (km/h): ", "type": float,}
    ],
    "Egyéb": []
}

def show_sport_menu():
    print("\nSportág: ")
    for key, name in SPORTS.items():
        print(f"{key}. {name}")

def choose_sport():
    show_sport_menu()
    choice = input("\nVálasztás: ")
    return SPORTS.get(choice, "Egyéb")

def ask_sport_details(sport):
    questions = SPORT_QUESTIONS.get(sport, [])

    details = {}

    if len(questions) > 0:
        print(f"\n{sport} - egyedi adatok: ")

    for question in questions:

        answer = input(question["question"])

        if question["type"] == int:
            answer = int(answer)

        elif question["type"] == float:
            answer = float(answer.replace(",", "."))

        details[question["key"]] = answer

    return details