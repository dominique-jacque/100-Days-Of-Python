print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island!\nYou're mission is to find the treasure. ")
# First decision
direction_decision = input("You're at a cross road. Where do you want to go? Left or Right? ").lower()

if direction_decision == "left":
    print("Good job avoiding the giant hole!")

    # Second decision
    swim_decision = input("You came across a river. Do you swim or do you wait? ").lower()
    if swim_decision == "wait":
        print("Good job! There was a crocodile waiting in the river!")

        # Third decision
        run_decision = input("But hold on, what's that? You hear someone in the area. Should you run or hide? ").lower()
        if run_decision == "run":
            print("Good job! You got away!")

            # Final decision
            door_decision = input("Now you came across three doors. Which one will you go through? Purple, Blue, or Red? ").lower()
            if door_decision == "red":
                print("You found the Treasure! YOU WON!")
            elif door_decision == "purple":
                print("It's a room full of snakes! Game Over")
            elif door_decision == "blue":
                print("It's a room full of tigers! Game Over!")
            else:
                print("You chose a door that doesn't exist! Game Over.")
        else:
            print("They captured you! Game Over.")
    else:
        print("A crocodile got you! Game Over.")
else:
    print("You fell into a hole! Game Over.")
