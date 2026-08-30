import json

from models.training import Training

FILE_NAME = "training.json"

def save_trainings(trainings):

    data=[]

    for training in trainings:

        training_data= {
            "date": training.date,
            "sport": training.sport,
            "training_type": training.training_type,
            "duration": training.duration,
            "focus": training.focus,
            "intensity": training.intensity,
            "exercises": training.exercises,
            "details": training.details
        }

        data.append(training_data)

    with open(FILE_NAME, "w", encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_trainings():

    try:
        with open(FILE_NAME, "r", encoding="UTF-8") as file:
            data = json.load(file)

    except FileNotFoundError:

        return []

    trainings = []

    for training_data in data:
        training = Training(
            training_data["date"],
            training_data.get("sport", "Muay Thai"),
            training_data["training_type"],
            training_data["duration"],
            training_data["focus"],
            training_data["intensity"],
            training_data.get("details", {})
        )

        training.exercises = training_data["exercises"]

        trainings.append(training)

    return trainings