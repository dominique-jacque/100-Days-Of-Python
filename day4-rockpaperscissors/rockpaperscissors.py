import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper =  '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand_images = [rock, paper, scissors]
player_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor "))
opponents_pick = random.randint(0, 2)
if player_pick == 0:
    print(rock)
    print(hand_images[opponents_pick])
    if opponents_pick == 0:
        print("It's a tie")
    elif opponents_pick == 2:
        print("You win!")
    else: 
        print("You lose!")
elif player_pick == 1:
    print(paper)
    print(hand_images[opponents_pick])
    if opponents_pick == 1:
        print("It's a tie")
    elif opponents_pick == 2:
        print("You lose!")
    else: 
        print("You win!")
elif player_pick == 2:
    print(scissors)
    print(hand_images[opponents_pick])
    if opponents_pick == 2:
        print("It's a tie")
    elif opponents_pick == 0:
        print("You lose!")
    else: 
        print("You win!")
else:
    print("You've entered the incorrect input. Let's try that again")