"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two value, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects value to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys  # This allows the reading of user input
import calendar
from datetime import datetime
import logging



value = len(sys.argv) - 1

date = datetime.now()
month = date.month
year = date.year

if (value == 0):
    print("No number submitted presenting system Month")

if (value==1):
    if(sys.argv[1].isnumeric()):

        month = sys.argv[1]
    else:
        print("must submit an integer value, please submit a months integer value") #need to handle error if 01,02,03 supplied currently does not handle that
elif (value == 2):
    if(sys.argv[2].isnumeric() & sys.argv[1].isnumeric()):

        month = sys.argv[1]
        year = sys.argv[2]
    else:
        print("must submit an integer value, please submit a months integer value and four digit year")#need to handle error if 01,02,03 supplied currently does not handle that


def calFun(month = month, year = year):
    cal = calendar.TextCalendar(calendar.MONDAY)
    printer = cal.formatmonth(year, month)
    print(printer)

calFun(int(month))
