# Make a dice code
# everytime user wants to roll they press R and you show random dice value everytime
# when user types S, you exit dice program.

import random 

while True:
    select=input("If you would like to roll the die, press R, and if you would like to stop, press S.................. ").lower()

    if select == "r":
        num = random.randint(1,6)
        print(f"You rolled.....{num}!")
    elif select == "s":
        break




