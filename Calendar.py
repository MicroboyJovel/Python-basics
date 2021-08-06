import calendar
import datetime
import time

print(calendar.weekheader(4))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2021,8))

print(calendar.monthcalendar(2021,8))
day_of_the_week = calendar.weekday(3000,8,6)

is_leap = calendar.isleap(2021)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000,3001)
print(how_many_leap_days)
