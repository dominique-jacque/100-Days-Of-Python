import random

# Exercise 1:  Heads or Tails
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
   print("Heads")
else:
    print("Tails") 

# Exercise 2: Who will pay the bill?
friends = ["Alex", "Beckham", "Jackie", "Tori", "Roy", "Naomi", "James"]
random_friend = random.choice(friends)

print(random_friend)