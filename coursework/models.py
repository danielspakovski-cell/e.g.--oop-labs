import json
from datetime import datetime

class Birthday:
    def __init__(self, name, date_str):
        self.name = name
        self.__date = datetime.strptime(date_str, "%Y-%m-%d")

    @property
    def date(self):
        return self.__date

class User:
    def __init__(self, username):
        self.username = username
        self.birthdays = [] 

    def add_birthday(self, birthday):
        self.birthdays.append(birthday)

    def save_birthdays_to_txt(self):
        filename = f"{self.username}_birthdays.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Vartotojo {self.username} gimtadienių sąrašas:\n")
            f.write("-" * 40 + "\n")
            for b in self.birthdays:
                f.write(f"Vardas: {b.name} | Data: {b.date.strftime('%Y-%m-%d')}\n")
        print(f"[Sistema]: Informacija išsaugota į {filename}")

    def notify_birthdays(self, factory):
        self.save_birthdays_to_txt()
        notifier = factory.create_notifier()
        today = datetime.now().strftime("%m-%d")
        
        for b in self.birthdays:
            if b.date.strftime("%m-%d") == today:
                notifier.send(f"Sveikiname, {b.name}! (Vartotojas: {self.username})")