from datetime import datetime, timedelta

def time_in_feature(date, start_hour, duration_in_hours):
    start_date = f"{date} {str(start_hour)}"
    start_time = datetime.strptime(start_date, "%d-%m-%Y %H")
    coming_time = start_time + timedelta(hours= duration_in_hours)
    coming_date = coming_time.date().strftime("%d-%m-%Y")
    coming_hour = coming_time.time().strftime("%H")
    print(f"Coming date : {coming_date}")
    print(f"Coming hour : {coming_hour}")

time_in_feature("9-12-2024", 17, 15)