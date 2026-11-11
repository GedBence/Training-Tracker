import json
from pathlib import Path
import os
import tempfile

from models.training import Training
from models.sport import Sport

FILE_NAME = Path(__file__).resolve().parents[1] / "training.json"


def write_json_safely(path, data):
    """Csak teljes, sikeres írás után cseréljük le a régi mentést."""
    content = json.dumps(data, ensure_ascii=False, indent=4)
    path = Path(path)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         delete=False) as file:
            temporary = Path(file.name)
            file.write(content)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()

def save_trainings(trainings):

    data=[]

    for training in trainings:

        training_data= {
            "date": training.date,
            "sport": str(training.sport),
            "duration": training.duration,
            "focus": training.focus,
            "intensity": training.intensity,
            "exercises": training.exercises,
            "details": training.details
        }

        data.append(training_data)

    write_json_safely(FILE_NAME, data)

def load_trainings():

    try:
        with open(FILE_NAME, "r", encoding="UTF-8") as file:
            data = json.load(file)

    except FileNotFoundError:

        return []

    except json.JSONDecodeError as error:
        raise ValueError(f"Sérült mentési fájl: {FILE_NAME}. Javítsd vagy állítsd vissza biztonsági másolatból; az eredeti fájlt nem írtuk felül.") from error

    trainings = []

    for training_data in data:
        sport = Sport(training_data.get("sport", "Muay Thai"))

        training = Training(
            training_data["date"],
            sport,
            training_data["duration"],
            training_data["focus"],
            training_data["intensity"],
            training_data.get("details", {})
        )

        training.exercises = training_data["exercises"]

        trainings.append(training)

    return trainings
