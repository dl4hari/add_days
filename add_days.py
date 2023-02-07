import datetime
from datetime import date

def add_days(n):
    business_days_to_add = n + 2
    current_date = date.today()
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date

print (date.today())
print (add_days(5))
