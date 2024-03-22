import random
import math
# Taking Inputs
lower = int(input("enter Lower bound:- "))

#Taking inputs
upper = int(input("Enter Upper bound:- "))

#Generating random number between
#the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the interger!\n")

#Initializing the number of guesses
count = 0

# for calc of min number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # condition testing
    if x == guess:
        print("Congrats you did it in ", count, " try")
        #once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed to high!")

#if guessing is more than required guesses,
#show this output
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\nBetter luck next time!")