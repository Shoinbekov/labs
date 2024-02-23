#exercise 1:
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date -timedelta(days=5)
print(current_date.strftime("%Y-%m-%d"))
print(new_date.strftime("%Y-%m-%d"))

#exercise 2:
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date -timedelta(days=1)
new_date2 = current_date + timedelta(days=1)
print(new_date.strftime("%Y-%m-%d"))
print(current_date.strftime("%Y-%m-%d"))
print(new_date2.strftime("%Y-%m-%d"))

#exercise 3:
import datetime 
time = datetime.datetime.today().replace(microsecond=0)
print(time)

#exercise 4:
from datetime import datetime
def date(date1, date2):
    time = date2 - date1

    diff = time.total_seconds()
    return diff

date_string1 = "2022-01-01 12:00:00"
date_string2 = "2022-02-01 15:30:45"
date1 = datetime.strptime(date_string1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_string2, "%Y-%m-%d %H:%M:%S")
difference_seconds = date(date1, date2)

print(f"The difference between the two dates is {difference_seconds} seconds.")