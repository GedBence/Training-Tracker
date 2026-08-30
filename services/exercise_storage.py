import json
from pathlib import Path

FILE_PATH = Path("data/costum_exercises.json")

def load_custom_exercises():
    if not FILE_PATH.exists():
        return {}

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_custom_exercises(exercises):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(exercises, file, ensure_ascii=False, indent=4)


def add_custom_exercise(sport, focus, exercise):
    print("DEBUG:", sport, focus, exercise)
    exercises = load_custom_exercises()

    if sport not in exercises:
        exercises[sport] = {}

    if focus not in exercises[sport]:
        exercises[sport][focus] = []

    if exercise not in exercises[sport][focus]:
        exercises[sport][focus].append(exercise)
        save_custom_exercises(exercises)
        return True

    return False