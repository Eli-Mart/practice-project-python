import random
#Library we use to generate random word

#ask user their name
name = input("What is your name? ")

#used to print statement and name variable
print("Good luck! ", name)

#Array of words
words = ["pony", "apple", "wrist", "python", "javascript",
        "computer", "rainbow", "mathematics", "college",
        "infinity", "beyond", "lightbulb", "water"]

#Function will choose random word from array
word = random.choice(words)

#statement giving user input
print("Guess the characters")

guesses = ""

#input any number of turns you wish to use
turns = 10

while turns > 0:

    #count the number of times user fails
    failed = 0

    #all characters from input one at a time
    for char in word:
        if char in guesses:
            print(char, end=" ")

        else:
            print("_")

            failed += 1

    if failed == 0:
        print("You win!")

        print("The word is: ", word)
        break

    print()
    guess = input("guess a character: ")

    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")

        print("You have", + turns, "more guesses")

        if turns == 0:
            print("You lose")

