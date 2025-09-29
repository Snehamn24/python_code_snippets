#we use the calendar.month(year,month) method to get the formatted calendar of the
#particular year and month

import calendar

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))

cal = calendar.month(year,month)
print(cal)
   
