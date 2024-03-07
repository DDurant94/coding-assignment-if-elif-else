'''
3. The Greatest Showdown
Objective:
Harness the power of conditional statements to compare and determine values.

Task 1: Identify the Greatest
Write a Python program that prompts the user to enter three numbers. The program should then identify and
 print out the largest number among the three.

Task 2: Identify the Smallest
Extend your program from Task 1 to also determine the smallest number among the three and print it out.

Task 3: Equality Check
Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like
 "Two numbers are equal and the largest" or "All numbers are equal".

'''

# I need three numbers to be input by user and some how compare the numbers and put them in a list from greatest to lowest.
# I am wondering if i can make a list and nest a ternery operator. used the inputs to make a list and compare the list to different conditions.
# i have a fix number of possiblities that i can get a result of.
# i need to figure out whatis the best way to nest this problem, i feel i have way to many lines of code out and about 



user_input = float(input("Enter in a number: "))
user_input2 = float(input("Enter in a second number: "))
user_input3 = float(input("Enter in a third number: "))

if user_input > user_input2 and user_input > user_input3:
  if user_input2 == user_input3:
   print("two numbers entered are the same", user_input2, "and", user_input, "is the largest number.")
  else:
    print(user_input, "is the largest number.")

elif user_input2 > user_input and user_input2 > user_input3:
  if user_input == user_input3:
     print("numbers", user_input, "and", user_input3, "are the same and", user_input2, "is the largest number.")
  else:
    print(user_input2, "is the largest number.")
elif user_input3 > user_input and user_input3 > user_input2:
  if user_input == user_input2:
    print("numbers", user_input, "and", user_input2, "are the same and", user_input3, "is the largest number.")
  else:
    print(user_input3, "is the largest number.")



if user_input < user_input2 and user_input < user_input3:
    if user_input2 == user_input3:
      print("numbers", user_input2, "and", user_input3, "are the same and", user_input, "is the smallest number.")
    else:
      print(user_input, "is the smallest number.")
elif user_input2 < user_input and user_input2 < user_input3:
    if user_input == user_input3:
     print("numbers", user_input, "and", user_input3, "are the same and", user_input2, "is the smallest number.")
    else:
      print(user_input2, "is the smallest number.")
elif user_input3 < user_input and user_input3 < user_input2:
    if user_input == user_input2:
      print("numbers", user_input, "and", user_input2, "are the same and", user_input3, "is the smallest number.")
    else:
      print(user_input3, "is the smallest number.")
elif user_input == user_input2 and user_input == user_input3:
   print("All three numbers are the same.")


   
#This gives me the right answer but I know that I have to be able to do this in a better way using the if, elif and else statement. 



