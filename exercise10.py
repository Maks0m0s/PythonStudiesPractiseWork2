from datetime import datetime

def calendar(events_dict):
    def add_event(dictionary):
        try:
            print("To add an event insert second information about an event :")
            day = int(input("Day : "))
            month = int(input("Month : "))
            year = int(input("Year : "))
            event_date = datetime(day= day, month= month, year= year)
            dictionary[event_date.strftime("%d-%m-%Y")] = input("Write an event :\n")
            print("Ready! You've added a new event.")
        except:
            print("Your date of event is wrong.")

    def show_event(dictionary):
        try:
            if len(dictionary.values()) > 0:
                print("To show you an event insert second information about an event :")
                day = int(input("Day : "))
                month = int(input("Month : "))
                year = int(input("Year : "))
                event_date = datetime(day=day, month=month, year=year)
                print(f"Your event :\n{dictionary[event_date.strftime("%d-%m-%Y")]}")
            else:
                print("You don't have any event.")
        except:
            print("You don't have any event on that day or your date of event is wrong.")


    try:
        action = int(input("\nWrite your action :\n"
                           "Show event - 1\n"
                           "Add event - 2\n"
                           "Quit - 3\n"))
        if action == 1:
            show_event(events_dict)
            return True
        elif action == 2:
            add_event(events_dict)
            return True
        elif action == 3:
            program_work = False
            return program_work
        else:
            raise Exception("You can choose only between 1 and 2.")
    except ValueError:
        print("You can write only integers.")
        return True
    except Exception as ex:
        print(ex)
        return True


events = dict()
program = True
while program:
    if calendar(events):
        program = True
    else:
        program = False
