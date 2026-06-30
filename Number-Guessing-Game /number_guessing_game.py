#Number Guessing Game
import random
lowest_number=5
Highest_number=65
secret=random.randint(lowest_number,Highest_number)
is_running=True
guesses=0
print("\n=====Welcome to python number guessing game!=====\n")
print(f"\n====Only number between {lowest_number} and {Highest_number}====.")
while is_running:
    guess=input("\nSelect a number between 5 and 65: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if lowest_number>guess or guess>Highest_number:
            print("\nSorry, you didn't guess correctly.")
            print(f"Only number between {lowest_number} and {Highest_number}. ")
        elif guess==secret:
             print(f"\nCorrect answer!.{guess}\n")
             print(f"\nNumber of guesses {guesses}.")
             is_running=False
        elif guess>secret:
            print("\nLower please.")
        elif guess<secret:
            print("\nHigher please.")
        else:
            print("\nInvalid answer.")
    else:
        print("\nSorry, you didn't guess correctly.")
