import random

#ask player their name
name = input('What is your name? ')
# print statement declaring name
print("Welcome to the Dice Rolling Simulator", name)

#Add while loop to function only if true
while True:
#input statement asking player dice quantity and sides
    num_dice = int(input("How many dice would you like to roll? "))
    num_sides = int(input("How many sides do the dice have? "))

# print statement of how many dice and sides are being rolled
    print("Rolling", num_dice, "dice with", num_sides, "sides each...")

#randomize result of dice(s) rolled
    total_value = 0
    for i in range(num_dice):
        roll_result = random.randint(1, num_sides)
        print("Die", i+1, ":", roll_result)
        total_value += roll_result

#print total result from roll
    print("Total value rolled: ", total_value)

#Ask player if they want to play again
    play_again = input("Would you like to roll again? (yes/no):  ")
    if play_again.lower() != "yes":
        print("Thank you for playing! Take care.")
        break    