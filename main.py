
# ==========================================
# MUAY THAI TRAINING TRACKER - V1
# ==========================================
from datetime import datetime
from models.training import Training
from data.sports import choose_sport, ask_sport_details, SPORT_QUESTIONS

from services.generator import generate_training_plan, choose_focus
from services.storage import save_trainings, load_trainings
from services.exercise_storage import add_custom_exercise

from utils.menu import show_menu

# ------------------------------------------
# ADATOK
# ------------------------------------------

trainings = load_trainings()

def get_valid_int(message, min_value=None, max_value=None, allow_empty=False):
    while True:
        user_input = input(message)

        if allow_empty and user_input == "":
            return None

        try:
            value = int(user_input)

            if min_value is not None and value < min_value:
                print(f"Az érték nem lehet kisebb, mint {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Az érték nem lehet nagyobb, mint {max_value}.")
                continue

            return value

        except ValueError:
            print("Kérlek, egész számot adj meg!")


def get_valid_date(message, allow_empty=False):
    while True:
    
        user_input = input(message)
    
        if allow_empty and user_input == "":
            return None

        try:
            datetime.strptime(user_input, "%Y.%m.%d")
            return user_input
        except ValueError:
            print("Hibás dátum! A helyes formátum: ÉÉÉÉ.HH.NN")
                
# ------------------------------------------
# ÚJ EDZÉS
# ------------------------------------------

def create_training():
    print("\n")
    print("=" * 40)
    print("ÚJ EDZÉS")
    print("=" * 40)

    sport = choose_sport()

    date = get_valid_date("Dátum (ÉÉÉÉ.HH.NN): ")

    training_type = input("Edzés típusa: ")

    duration = get_valid_int(
        "Időtartam (perc): ",
        min_value=1
    )

    focus = choose_focus(sport)

    intensity = get_valid_int(
        "Intenzitás (1-10): ",
        min_value=1,
        max_value=10
    )

    details = ask_sport_details(sport)

    training = Training(
        date,
        sport,
        training_type,
        duration,
        focus,
        intensity,
        details)

    print("\nMost add hozzá az edzés gyakorlatait.")

    while True:

        exercise = input("\nGyakorlat (ENTER = befejezés): ").strip()

        if exercise == "":
            break

        training.add_exercise(exercise)

        added = add_custom_exercise(sport, focus, exercise)

        if added:
            print("Új gyakorlat hozzáadva a gyakorlatlistához.")

        print("✓ Gyakorlat hozzáadva!")

    trainings.append(training)

    save_trainings(trainings)

    print("\n✓ Edzés sikeresen elmentve!")

# ------------------------------------------
# EDZÉSEK MEGTEKINTÉSE
# ------------------------------------------

def show_trainings():

    print("\n")
    print("=" * 40)
    print("ELMENTETT EDZÉSEK")
    print("=" * 40)

    if len(trainings) == 0:
        print("Még nincs egyetlen edzés sem.")

        return

    for number, training in enumerate(trainings, start=1):
        print(f"\n[{number}]")

        training.show_training()

# ------------------------------------------
# STATISZTIKA
# ------------------------------------------

def show_statistics():

    print("\n")
    print("=" * 40)
    print("STATISZTIKA")
    print("=" * 40)

    if len(trainings) == 0:

        print("Még nincs elegendő adat.")

        return

    total_training_time = 0

    total_intensity = 0

    sport_counts= {}

    for training in trainings:
        (total_training_time) += int(training.duration)

        (total_intensity) += int(training.intensity)

        sport_counts[training.sport] = sport_counts.get(training.sport, 0) + 1

    average_intensity = (total_intensity / len(trainings))

    print(
        f"Összes edzés: "
        f"{len(trainings)}"
    )

    print(
        f"Összes edzésidő: "
        f"{total_training_time} perc"
    )

    print(
        f"Átlagos intenzitás: "
        f"{average_intensity:.1f}/10"
    )

    print("\nEdzések sportáganként: ")
    for sport, count in sport_counts.items():
        print(f"- {sport}: {count} db")

# ------------------------------------------
# MENÜ MÓDOSÍTÁS
# ------------------------------------------

def select_training():

    if len(trainings) == 0:
        print("\nMég nincs edzésed.")
        return None

    show_trainings()

    try:
        index = int(input("\nMelyik edzést választod? (sorszám): "))

    except ValueError:
        print("\n Érvénytelen sorszám!")
        return None

    if index < 1 or index > len(trainings):
        print("\nNincs ilyen sorszámú edzés.")
        return None

    return index -1

# ------------------------------------------
# EDZÉS SZERKESZTÉS
# ------------------------------------------

def edit_training():
    print("\n")
    print("=" * 40)
    print("EDZÉS SZERKESZTÉSE")
    print("=" * 40)

    index = select_training()

    if index is None:
        return

    training = trainings[index]

    print("\nHagyd üresen (ENTER), ha nem akarod módosítani az adot mezőket.")

    new_date = get_valid_date(
        f"\nDátum ({training.date})",
        allow_empty=True)

    if new_date is not None:
        training.date = new_date

    new_type = input(f"\nEdzés típusa ({training.training_type}): ")
    if new_type != "":
        training.training_type = new_type

    new_duration = get_valid_int(
        f"\nIdőtartam ({training.duration}): ",
        min_value=1,
        allow_empty=True
    )

    if new_duration is not None:
        training.duration = new_duration


    new_focus = input(f"\nEdzés fókusza ({training.focus}): ")
    if new_focus != "":
        training.focus = new_focus

    new_intensity = get_valid_int(
        f"\nIntenzitás ({training.intensity}): ",
        min_value=1,
        max_value=10,
        allow_empty=True
    )

    if new_intensity is not None:
        training.intensity = new_intensity

    questions = SPORT_QUESTIONS.get(training.sport, [])

    if len(questions) > 0:
        print(f"\n{training.sport} - egyedi adatok szerkesztése:")

    for question in questions:
        key = question["key"]
        current_value = training.details.get(key, "nincs megadva")

        answer = input(f"{question['question'].strip()} ({current_value})")

        if answer != "":

            try:
                if question["type"] == int:
                    answer = int(answer)

                elif question["type"] == float:
                    answer = float(answer.replace(",", "."))

                training.details[key] = answer

            except ValueError:
                print(f"Érvénytelen érték, '{key}' mező nem módosult")

    save_trainings(trainings)

    print("\nEdzés sikeresen módosítva!")

# ------------------------------------------
# EDZÉS TÖLRÉSE
# ------------------------------------------

def delete_training():

    print("\n")
    print("=" * 40)
    print("EDZÉS TÖRLÉSE")
    print("=" * 40)

    index = select_training()

    if index is None:
        return

    training = trainings[index]

    confirm = input(f"\nBiztos törlöd ezt az edzést? ({training.date} - {training.sport}) (i/n):")

    if confirm.lower() == "i":
        trainings.pop(index)
        save_trainings(trainings)
        print("\nEdzés sikeresen törölve!")

    else:
        print("\nTörlés sikertelen.")



# ------------------------------------------
# PROGRAM
# ------------------------------------------
 
while True:

    show_menu()

    choice = input("\nVálasztás: ")

    if choice == "1":
        create_training()

    elif choice == "2":
        show_trainings()

    elif choice == "3":
        show_statistics()

    elif choice == "4":
        generate_training_plan()

    elif choice == "5":
        edit_training()

    elif choice == "6":
        delete_training()

    elif choice == "0":

        print("\nKilépés a programból.")

        break

    else:

        print("\n❌ Érvénytelen választás!")

