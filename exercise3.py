from datetime import datetime, timedelta

def check_passed_time():
    now = datetime.now()
    starter = input("You've just created a file press any button whenever you want :\n")
    after = datetime.now()
    difference = after - now
    ten_hours = timedelta(hours= 10)
    if difference > ten_hours:
        print("Since file was created already passed more than 10 HOURS !!!")
    else:
        print("Time that passed since file was created :")
        print(difference)

check_passed_time()