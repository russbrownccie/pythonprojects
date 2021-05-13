# This is a program to roll 1 million pair of dice rolls and trace the numbers rolled for each from two through twelve
# and what the expected number would be in a perfectly distributed roll
# for example a 2 or 12 should occur 1/36 times, 3 or 11 2/36, etc up to 7 which should occur 1/6th of the time.

# sets variables
import random

two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0
diceroll = 0

# rolls dice, adds the sum, and sets it to the variable count

for items in range(1000000):
    total = random.randint(1, 6) + random.randint(1, 6)
    diceroll += 1
    if total == 2:
        two += 1
    elif total == 3:
        three += 1
    elif total == 4:
        four += 1
    elif total == 5:
        five += 1
    elif total == 6:
        six += 1
    elif total == 7:
        seven += 1
    elif total == 8:
        eight += 1
    elif total == 9:
        nine += 1
    elif total == 10:
        ten += 1
    elif total == 11:
        eleven += 1
    elif total == 12:
        twelve += 1

# prints the output

print(f"The value of 2 is {two} and the expected value is {round(diceroll * 0.02778)}")
print(f"The value of 3 is {three} and the expected value is {round(diceroll * 0.05556)}")
print(f"The value of 4 is {four} and the expected value is {round(diceroll * 0.08333)}")
print(f"The value of 5 is {five} and the expected value is {round(diceroll * 0.11111)}")
print(f"The value of 6 is {six} and the expected value is {round(diceroll * 0.13889)}")
print(f"The value of 7 is {seven} and the expected value is {round(diceroll * 0.16667)}")
print(f"The value of 8 is {eight} and the expected value is {round(diceroll * 0.13889)}")
print(f"The value of 9 is {nine} and the expected value is {round(diceroll * 0.11111)}")
print(f"The value of 10 is {ten} and the expected value is {round(diceroll * 0.08333)}")
print(f"The value of 11 is {eleven} and the expected value is {round(diceroll * 0.05556)}")
print(f"The value of 12 is {twelve} and the expected value is {round(diceroll * 0.02778)}")
