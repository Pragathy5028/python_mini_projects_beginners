# rand int vs rand range=rand int incldes the upper bound while rand range dosent

import random
upper_bound=input("Enter a number:\n")

if upper_bound.isdigit():
    upper_bound=int(upper_bound)

    if upper_bound<0:
        print("Enter a positive number next time")
        quit()
else:
        print("Enter a number next time")
        quit()
random_number= random.randint(0,upper_bound)
guess=0

while True:
    guess+=1
    user_guess=input("make a guess:\n")
    if user_guess.isdigit():
        user_guess=int(user_guess)
 
    else:
        print("Enter a number next time")
        continue

    if user_guess==random_number:
        print("you got it right!")
        break
    elif user_guess>random_number:
        print("you were above the number.Try again!")
    else:
        print("You were below the number. Try again!")
    
print(f"You made {guess} guesses")




