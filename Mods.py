import random
def calculator():
    print("Welcome to the calculator")
    print("Please select your operation")
    ch = input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division: ")
    if ch == "Addition" or "addition":
        x = int(input("First number: "))
        y = int(input("Second number: "))
        print(x+y)
    elif ch == "Subtraction" or "subtraction":
        x = int(input("First number: "))
        y = int(input("Second number: "))
        print(x-y)
    elif ch == "Multiplication" or "multiplication":
        x = int(input("First number: "))
        y = int(input("Second number: "))
        print(x*y)
    # Division is not working please help
    elif ch == "Division" or "division":
        x = int(input("First number: "))
        y = int(input("Second number: "))
        print(x/y)

def numberGuessingGame():
    print("Welcome to the number guessing game")
    while True:
      num = random.randint(1, 10)
      o = int(input("Guess a number from 1 to 10: "))
      if o == num:
         print("Good job!")
         break
      else:
         print("Try again")