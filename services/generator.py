# ------------------------------------------
# RANDOM EDZÉSTERV GENERÁLÁSA
# ------------------------------------------

import random

from data.sports import choose_sport
from data.exercises import EXERCISE_POOLS
from services.exercise_storage import load_custom_exercises


def get_exercise_pools(sport):
    sport = str(sport)
    pools = {}

    base_pools = EXERCISE_POOLS.get(sport, {})

    for focus, exercises in base_pools.items():
        pools[focus] = exercises.copy()

    custom_exercises = load_custom_exercises()
    custom_pools = custom_exercises.get(sport, {})

    for focus, exercises in custom_pools.items():
        if focus not in pools:
            pools[focus] = []

        for exercise in exercises:
            if exercise not in pools[focus]:
                pools[focus].append(exercise)

    return pools


def choose_focus(sport):
    pools = get_exercise_pools(sport)

    focus_options = list(pools.keys())

    print("\nEdzés fókusza:")

    for number, focus in enumerate(focus_options, start=1):
        print(f"{number}. {focus}")

    print(f"{len(focus_options) + 1}. Új fókusz")

    while True:
        choice = input("\nVálasztás: ")

        try:
            choice_number = int(choice)

            if 1 <= choice_number <= len(focus_options):
                return focus_options[choice_number - 1]

            if choice_number == len(focus_options) + 1:
                new_focus = input("Új fókusz neve: ").strip()

                if new_focus != "":
                    return new_focus

                print("A fókusz neve nem lehet üres.")

            else:
                print("Érvénytelen választás!")

        except ValueError:
            print("Kérlek, számot adj meg!")


def generate_training_plan():

    print("\n")
    print("=" * 40)
    print("RANDOM EDZÉSTERV GENERÁTOR")
    print("=" * 40)

    sport = choose_sport()

    pools = {focus: drills for focus, drills in get_exercise_pools(sport).items() if drills}

    if not pools:
        print(f"\n '{sport}' sportághoz még nincs edzésterv-generátor.")
        return

    focus_options = list(pools.keys())

    print("\nFókusz:")
    for number, focus_name in enumerate(focus_options, start=1):
        print(f"  {number}. {focus_name}")
    print(f"{len(focus_options) + 1}. Random (mindegyikből egy kicsit)")

    focus_choice = input("\nVálasztás: ")

    try:
        choice_number = int(focus_choice)

    except ValueError:
        print("\nÉrvénytelen választás!")
        return

    print("\n")
    print("=" * 40)
    print("GENERÁLT EDZÉSTERV")
    print("=" * 40)

    print("\n Bemelegítés - 10 perc")

    if 1 <= choice_number <= len(focus_options):

        selected_focus = focus_options[choice_number - 1]

        print(f"\n {selected_focus.upper()}")

        drills = pools[selected_focus]
        sample_size = min(3, len(drills))

        for drill in random.sample(drills, sample_size):
            print(f" - {drill}")

    elif choice_number == len(focus_options) + 1:
        print("\n RANDOM EDZÉSTERV")

        for focus_name, drills in pools.items():
            drill = random.choice(drills)
            print(f"- {focus_name}: {drill}")

    else:

        print("\n❌ Érvénytelen választás!")
        return

    # Levezetés
    print("\n Levezetés - 5 perc")

    print("\n" + "=" * 40)
    print("✓ EDZÉSTERV ELKÉSZÜLT!")
    print("=" * 40)
