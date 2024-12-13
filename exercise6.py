from datetime import datetime, timedelta

def birthday_check(birthday):
    date = datetime.strptime(birthday, "%d-%m-%Y")
    if date.weekday() == 5 or date.weekday() == 6:
        print("Congratulations ! You were born on the weekend.")
    else:
        print("Your birthday is not on the weekend :(")

birthday_check("15-02-2010")