'''
2. The Story Brancher
Task 1: Code Correction
You are provided with a Python script that uses if-else structures for a story branching mechanism. There are some errors in the code. Identify and correct them.

Buggy Code:

choice = input("Do you choose the path to the left or right? ")

if choice = "left":
    print("You find a treasure chest!")
elif choice = "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")
'''

choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")