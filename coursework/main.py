from models import User, Birthday
from services import EmailFactory, SMSFactory

def run_app():
    jonas = User("Jonas")
    jonas.add_birthday(Birthday("Petras", "1990-04-24")) 
    
    marija = User("Marija")
    marija.add_birthday(Birthday("Ana", "1995-04-24"))  

    email_factory = EmailFactory()
    sms_factory = SMSFactory()
    
    print(f"--- Vykdomi procesai vartotojui {jonas.username} ---")
    jonas.notify_birthdays(email_factory)

    print(f"\n--- Vykdomi procesai vartotojui {marija.username} ---")
    marija.notify_birthdays(sms_factory)

if __name__ == "__main__":
    run_app()