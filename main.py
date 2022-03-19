import Mods
# This is the computer which uses mods.py as features and a sign up and log in page
# Read then comment down here
# Your comment
if_acc = 0
acc = "Nan"
def createacc():
    if_acc = 0
    print("Welcome to test website")
    if if_acc == 0:
        print("You do not have an account")
        print("Create an account by typing yes")
    x = input("here ")
    if x == "yes":
        a = input("Username: ")
        b = int(input("Password: "))
        if_acc += 1
        acc = a + str(b) and 1
    print("You have created a new account")
    print("Your account is: " + a)
    print("Make sure to verify by logging in")
    o = input("Do you want to log in? ")
    if o == "yes":
        c = input("Username: ")
        if c != a:
            print("Wrong username. Please try again by restarting")
            quit()
        d = int(input("Password: "))
        if d != b:
            print("Wrong password. Please try again by restarting")
            quit()
        if c == a and d == b:
            print("You are logged in as " + a)

if if_acc == 0:
    createacc()
    if_acc = 1

if if_acc == 1:
   print("Welcome to the computer. Please select an application")
   o = input("1.Calculator\n2.Number guessing game: ")
   if o == "Calculator" or "calculator":
       Mods.calculator()
   if o == "number guessing game" or "Number guessing game":
       Mods.numberGuessingGame()