from datetime import date

class HealthMetric:
    def __init__(self, entry_date, steps,calories, sleep_hours, mood):
        self.entry_date = entry_date
        self.steps = steps
        self.calories = calories
        self.sleep_hours = sleep_hours
        self.mood = mood


    def show_summary(self):
        print(f"📅 {self.entry_date} | Steps: {self.steps}, Calories: {self.calories}, Sleep: {self.sleep_hours}h, Mood: {self.mood}")
    

    def self_dict(self):
        return {"entry_date":self.entry_date,
               "steps":self.steps,
               "calories":self.calories,
               "sleep_hours":self.sleep_hours,
               "mood":self.mood}
