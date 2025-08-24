#Rock Paper Scissors Game
import random
choices=["rock","paper","scissors"]
print("Welcome to ROCK,PAPER,SCISSORS Game!")
while True:
    user=input("Enter your choice(rock,paper,scissors)or 'exit' to quit:").lower()
    if user=="exit":
        print("Thanks for playing Goodbye!")
        break
    if user not in choices:
        print("Invalid choice.Please try again.")
        continue
    computer=random.choice(choices)
    print(f"Computer chose:{computer}")
    if user==computer:
        print("It's tie")
    elif user=="rock" and computer=="scissors":
        print("you win")
    elif user=="paper" and computer=="rock":
        print("you win")
    elif user=="scissors" and computer=="paper":
        print("you win")
    else:
        print("computer wins")
