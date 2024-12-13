from datetime import datetime, timedelta

def mondayGeneretor(date1, date2):
    start_date = datetime.strptime(date1, "%d-%m-%Y")
    finish_date = datetime.strptime(date2, "%d-%m-%Y")
    while start_date <= finish_date:
        if start_date.weekday() == 0:
            result = datetime.strftime(start_date, "%d-%m-%Y")
            print(result)
        start_date += timedelta(days=1)

mondayGeneretor("13-12-2024", "1-1-2025")
