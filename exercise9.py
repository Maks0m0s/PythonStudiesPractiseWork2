from datetime import datetime, timedelta

def work_hours_counter(date1, date2, amount_of_hours_for_day):
    start_date = datetime.strptime(date1, "%d-%m-%Y")
    finish_date = datetime.strptime(date2, "%d-%m-%Y")
    result_amount_of_hours = 0
    while start_date <= finish_date:
        if start_date.weekday() != 5 and start_date.weekday() != 6:
            result_amount_of_hours += amount_of_hours_for_day
            print(start_date)
        start_date += timedelta(days= 1)
    print(f"Total work hours : {result_amount_of_hours}")

work_hours_counter("1-12-2024", "1-1-2025", 8)