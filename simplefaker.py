import random
from datetime import datetime, timedelta

class SimpleFaker:
    def __init__(self):
        self.first_names_male = ["John", "James", "Robert", "Michael", "William"]
        self.first_names_female = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth"]
        self.last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown"]
        self.countries = ["USA", "Canada", "UK", "Australia", "South Africa", "Jamaica", "Tanzania"]
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def name(self, sex='male'):
        if sex == 'male':
            first_name = random.choice(self.first_names_male)
        elif sex == 'female':
            first_name = random.choice(self.first_names_female)

        last_name = random.choice(self.last_names)
        return f"{first_name} {last_name}"

    def sex(self):
        return random.choice(['male', 'female'])

    def country(self):
        return random.choice(self.countries)

    def date_of_birth(self, minimum_age=18, maximum_age=40):
        start_date = datetime.now() - timedelta(days=365 * maximum_age)
        end_date = datetime.now() - timedelta(days=365 * minimum_age)
        return self.random_date(start_date, end_date)

    def random_date(self, start, end):
        return start + timedelta(days=random.randint(0, (end - start).days))

    def event_name(self):
        sports = ["Swimming", "Diving", "Water Polo", "Athletics", "Gymnastics"]
        return random.choice(sports)

    def venue(self):
        return f"Stadium {random.choice(self.letters)}"

    def year(self):
        return random.randint(990, 1012) * 2 # Only even numbers

    def season(self, year = None):
        if year % 4 == 0:
          return 'summer'
        elif year % 4 == 2:
          return 'winter'
        return random.choice(['summer', 'winter'])
