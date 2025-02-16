
 # Exercise 1

print("Welcome to the Fun Rollercoaster Ride!")
height = int(input("How tall are you in cm? "))
bill = 0
if height >= 120:
    print("Enjoy the ride!")
    age = int(input(" But first, how old are you? " ))
    if age >= 18:
        bill = 12
        print("Adult tickets are $12")
    elif age <= 12:
        bill = 5
        print("Child tickets are $5")
    else:
       bill = 7
       print("Youth tickets are $7")

    wants_photo = input("Do you want to have your photo taken? Type y for yes or n for no: ")
    if wants_photo == "y":
        bill += 3 # bill = bill + 3
    print(f"Your final bill is {bill}")

else:
    print("I'm sorry, you need to grow a little more before entering this ride. ")

# Exercise 2

print("Welcome to the Python Pizza Delieveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extracheeze? Y or N: ")

#todo: work out how much they need to pay based on their size choice
bill = 0
if size == "S":
    bill += 15
elif size == "L":
    bill += 20
elif size == "M":
    bill += 17
else:
    print("You typed the wrong inputs.")


#todo: work out how much to add their bill based on their pepperoni choice. 
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

#todo: work out their final amount based on whether if they want extra cheese. 
if extra_cheese == "Y":
    bill += 1
print(f"Your total amount is: ${bill}")
