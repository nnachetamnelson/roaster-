import datetime

def generate_roster(employees):
    roster = {}
    for employee in employees:
        roster[employee] = []
        current_date = datetime.datetime.now().date()
        while len(roster[employee]) < 7:
            if current_date.weekday() not in [5, 6]: # if not saturday or sunday
                if current_date.hour < 15: # if before 3 PM
                    roster[employee].append(current_date)
                elif current_date.hour >= 19: # if after 7 PM
                    roster[employee].append(current_date)
            current_date += datetime.timedelta(days=1)
    return roster

employees = ['Alice', 'Bob', 'Charlie', 'David']
roster = generate_roster(employees)
print(roster)
