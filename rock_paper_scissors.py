
import random


user_points=0
computer_points=0
options=["rock","paper","scissors"]



while True:
    user_pick=input("Type rock, paper ,scissors or Q to quit: ").lower()
    if user_pick=='q':
        break
    if user_pick not in options:
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print(f"computer picked {computer_pick} ")

    if user_pick=="rock" and computer_pick=="scissors":
        print("You won!")
        user_points+=1
    elif user_pick=="scissors" and computer_pick=="paper":
        print("You won!")
        user_points+=1
    elif user_pick=="paper" and computer_pick=="rock":
        print("You won!")
        user_points+=1
    else:
        print("computer won")
        computer_points+=1
print(f"You won {user_points} times")
print(f"Computer won {computer_points} times")
print("Goodbye!")

