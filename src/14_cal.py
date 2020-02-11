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
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
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

currentMonth = datetime.today().month
currentYear = datetime.today().year
cal = calendar.TextCalendar(calendar.SUNDAY)

userInput = input()

def monthYearInputDate(userMonth, userYear):return cal.formatmonth(userYear, userMonth) + cal.formatyear(userYear, userMonth)


def noInputDate():return cal.formatmonth(currentYear, currentMonth)

def monthInputDate(userMonth=userInput.isnumeric()):return cal.formatmonth(currentYear, userMonth)

if len(userInput) == 0:
    print(noInputDate())

elif 13 > int(userInput) > 0 and len(userInput)<3 :
    x = int(userInput)
    print(monthInputDate(x))


elif int(len(userInput))> 3 :
    m, y = userInput.split(',')
    m, y = int(m), int(y)
    print(monthYearInputDate(m, y))

else:
    print("Please input a month or year as a number")








