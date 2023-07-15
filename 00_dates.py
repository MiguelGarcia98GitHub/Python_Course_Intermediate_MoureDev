# Dates

from datetime import datetime

now = datetime.now()



print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()

print(timestamp)

year_2023 = datetime(2023, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print_date(year_2023)

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

from datetime import timedelta

time_delta = timedelta()

diff = year_2023.date() - current_date

print(diff)

init_timedelta = timedelta(200, 100, 100, 10)
print(init_timedelta)