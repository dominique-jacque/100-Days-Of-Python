
 # Example
print("Welcome to the Fun Rollercoaster Ride!")
height = int(input("How tall are you in cm? "))
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
       
       
    
    wants_photo = input("Do you want to have your photo taken? Type y for yes or n for no")
    if wants_photo == "y":
        bill += 3 # bill = bill + 3

    print(f"Your final bill is {bill}")
else:
    print("I'm sorry, you need to grow a little more before entering this ride. ")