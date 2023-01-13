 import datetime

def generate_roster(employees):
    roster = {}
    for employee in employees:
        roster[employee] = []
        current_date = datetime.datetime.now().date()
        days_worked = 0
        while days_worked < 7:
            if current_date.weekday() not in [5, 6]: # if not saturday or sunday
                current_time = datetime.time(7, 0) # 7 AM
                current_datetime = datetime.datetime.combine(current_date, current_time)
                if current_datetime.hour < 15: # if before 3 PM
                    current_time = datetime.time(19, 0) # 7 PM
                    current_datetime = datetime.datetime.combine(current_date, current_time)
                    if current_datetime.hour >= 19:
                        roster[employee].append(current_date)
                        days_worked += 1
                if days_worked % 7 == 6: # if employee has worked 6 days in a row
                    current_date += datetime.timedelta(days=1) # give employee a day off
            current_date += datetime.timedelta(days=1)
    return roster

employees = ['Alice', 'Bob', 'Charlie', 'David']
roster = generate_roster(employees)
print(roster)
