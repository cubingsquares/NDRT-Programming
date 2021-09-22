# Python with Pat Week 1 Challenge 3

# Goal: (Advanced) Write a guessing game. You should let the user type a guess between 1 and 100, 
# and then tell the user if they are too high, too low, or correct.
# For this one, you’ll need the “input” function to get user input, 
# and the “random” library to generate random numbers. Talk to me for help with this one.

# Name: Jack Kalicak
# Date: 19 September 2021
# Python with Pat Week 1 Challenge 1

import random
number = random.randint(1, 100)
guess = -1
N= 0


while guess != number:
    guess = int(input('Enter your guess: '))
    if guess <= number:
        print('Too low')
        N= N+1
    elif guess < number:
        print('Too high')
        N= N+1
    else: 
        print('Yay you won in: ' + str(N) + ' guesses') 

    