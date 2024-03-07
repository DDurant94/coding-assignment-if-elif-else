'''
Task 1: Leap Year Checker
Write a Python program that prompts the user to input a year. The program should determine if the given year is 
a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: 
Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, 
but these centurial years are leap years if they are exactly divisible by 400.

Task 2: Century Verification
Add functionality to your program from Task 1 to inform the user if the entered year is 
a century year (e.g., 1900, 2000) regardless of whether it's a leap year or not.

Task 3: Time Traveler
Enhance your program to indicate if the provided year is in the future, past, or is the current year, 
compared to the a year variable year=2020.
'''

year = int(input("Enter a year! "))
current_year = 2020

if year % 400 == 0 and year % 100 == 0: # dividing the year entered by 400 and 100 to see if anything is left with %. If the year comes back with 0 we know 
  print( year, "is a leap year.")       # that it is a leap year.
elif year % 4 == 0 and year % 100 != 0: # on this line we see if the year can be divided by 4 and have 0 as a remainder and if the year
  print(year, "is a leap year.")        #  can be divided by 4 and the year is divided by 100 remainder isn't
else:                                   # equal to 0 it's a leap year.
  print(year, "is not a leap year.")



if year % 100 == 0: #if the year can be divided by 100 print its a century year.
  print(year, "is also a century year!")
else:
  print(year, "is also not a century year!")

if year > current_year:
  print(year, "is", year - current_year, "years in the future")
elif year == current_year:
  print(year, "is the current year!")
else:
  print(year, "is", current_year - year, "in the past!")