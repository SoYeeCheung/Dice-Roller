#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
def play():
    playchoice = str(input("Are you ready to roll? "))
    while not (playchoice.lower().startswith("y") or playchoice.lower().startswith("n")):
        playchoice = input("Are you ready to roll? ")
    return playchoice.lower().startswith("y")
        
def replay():
    replaychoice = str(input("Do you want to roll again? "))
    while not (replaychoice.lower().startswith("y") or replaychoice.lower().startswith("n")):
        replaychoice = str(input("Do you want to roll again? "))
    return replaychoice.lower().startswith("y")


print("Welcome to Dice Roller!!!")

if play():
    game_on = True
else:
    game_on = False
while game_on:
    cap = int(input("How many faces are there in your die? " ))
    print(random.randint(1,cap+1))
    if replay():
        game_on = True
    else:
        break

print("Game ended")

