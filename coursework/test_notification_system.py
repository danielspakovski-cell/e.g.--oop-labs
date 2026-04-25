import unittest
import os
from datetime import datetime
from models import User, Birthday

class TestBirthday(unittest.TestCase):

    def test_valid_date_parsing(self):
        b = Birthday("Testas", "1995-06-15")
        self.assertEqual(b.date.year, 1995)
        self.assertEqual(b.date.month, 6)
        self.assertEqual(b.date.day, 15)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            Birthday("Klaida", "15-06-1995")

class TestUserLogic(unittest.TestCase):

    def setUp(self):
        self.user = User("Testuotojas")

    def test_add_birthday(self):
        self.user.add_birthday(Birthday("Petras", "1990-01-01"))
        self.assertEqual(len(self.user.birthdays), 1)
        self.assertEqual(self.user.birthdays[0].name, "Petras")

    def test_txt_file_creation(self):
        self.user.add_birthday(Birthday("Ana", "1980-05-05"))
        self.user.save_birthdays_to_txt()
        
        filename = "Testuotojas_birthdays.txt"
        self.assertTrue(os.path.exists(filename), "Failas nebuvo sukurtas!")
        
        if os.path.exists(filename):
            os.remove(filename)

    def test_notification_logic_filtering(self):
    
        today_str = datetime.now().strftime("%Y-%m-%d")
        b_today = Birthday("Šiandienininkas", today_str)
        b_future = Birthday("Ateities", "2025-12-31")
        
        self.user.add_birthday(b_today)
        self.user.add_birthday(b_future)
        
        today_mm_dd = datetime.now().strftime("%m-%d")
        
        results = [b for b in self.user.birthdays if b.date.strftime("%m-%d") == today_mm_dd]
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Šiandienininkas")

if __name__ == "__main__":
    unittest.main()