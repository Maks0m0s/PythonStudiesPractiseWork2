from datetime import datetime, timedelta

def generate_calendar(year, month):
    date = datetime(year, month, 1)
    first_day = datetime(year, month, 1)
    start_day = first_day.weekday()
    num_of_days = 0

    if month == 12:
        next_month = datetime(year + 1, 1, 1)
        last_day = next_month - timedelta(days= 1)
        num_of_days = last_day.strftime("%d")
    elif month > 0 and month < 12:
        next_month = datetime(year, month + 1, 1)
        last_day = next_month - timedelta(days=1)
        num_of_days = last_day.strftime("%d")

    print(f"{date.strftime("%m-%Y")}\n")
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Printing spaces
    for _ in range(start_day):
        print("   ", end=" ")

    # Printing first week
    current_day = 1
    for day in range(start_day, 7):
        print(f"  {current_day}", end=" ")
        current_day = current_day + 1
    print()
    #Printing other weeks
    for day in range(current_day, int(num_of_days) + 1):
        print(f"{day}", end="  ")
        if (day + start_day) % 7 == 0:  # Line break at the end of the week
            print()

generate_calendar(2024, 12)