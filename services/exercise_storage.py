import json
from pathlib import Path
from services.storage import write_json_safely

FILE_PATH = Path(__file__).resolve().parents[1] / "data" / "costum_exercises.json"

def load_custom_exercises():
    if not FILE_PATH.exists():
        return {}

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError(f"Sérült gyakorlatlista: {FILE_PATH}. A fájlt nem írtuk felül.") from error


def save_custom_exercises(exercises):
    write_json_safely(FILE_PATH, exercises)


def add_custom_exercise(sport, focus, exercise):
    exercises = load_custom_exercises()

    sport_name = str(sport)

    if sport_name not in exercises:
        exercises[sport_name] = {}

    if focus not in exercises[sport_name]:
        exercises[sport_name][focus] = []

    if exercise not in exercises[sport_name][focus]:
        exercises[sport_name][focus].append(exercise)
        save_custom_exercises(exercises)
        return True

    return False
