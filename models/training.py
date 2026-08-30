# ------------------------------------------
# TRAINING CLASS
# ------------------------------------------

class Training:
    def __init__(self, date, sport, training_type, duration, focus, intensity, details=None):
        self.date = date
        self.training_type = training_type
        self.sport = sport
        self.duration = duration
        self.focus = focus
        self.intensity = intensity
        self.exercises = []
        self.details = details if details is not None else {}


    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def show_training(self):

        print("\n" + "=" * 40)
        print("EDZÉS")
        print("=" * 40)

        print(f"Sportág: {self.sport}")
        print(f"Dátum: {self.date}")
        print(f"Típus: {self.training_type}")
        print(f"Időtartam: {self.duration} perc")
        print(f"Fókusz: {self.focus}")
        print(f"Intenzitás: {self.intensity}/10")

        if len(self.details) > 0:
            print("\nEgyedi adatok: ")
            for key, value in self.details.items():
                print(f"- {key}: {value}")

        print("\nGyarkolatok:")

        if len(self.exercises) == 0:
            print("- Nincs hozzáadott gyarkolat.")

        else:
            for number, exercise in enumerate(self.exercises, start=1):
                print(f"{number}. {exercise}")

        print("=" * 40)
