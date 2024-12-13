from datetime import datetime, timedelta
import time

def countdown(date):
    passed_date = datetime.strptime(date, "%d-%m-%Y %H-%M-%S")
    while True:
        print(passed_date)
        passed_date -= timedelta(seconds= 1)
        time.sleep(1)

countdown("13-12-2024 18-49-00")