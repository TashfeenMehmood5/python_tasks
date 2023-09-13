#number guessing game

import random                 # module to return random number in between given range

num = random.randint(1, 10)   # randint( ) to get a random integer value from user
guess = None                  # guess variable is initially empty

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")