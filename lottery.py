# Powerball Lottery Simulator - v 0.1
# Written by Russ Brown for Python Crash Course project
# This program attempts to continuously draw for powerball until it gets a match on the MY_TICKET variable
# Powerball draws 5 numbers from a pool of white balls 1-69 and one red ball 1-26
# This program saves those as a dictionary, and then loops.   When the entire drawing is done, it compares tickets
# The program will tell you how long it took and how many tries - 400 million tries could take up to an hour on mine
# Written totally for fun - gambling is bad, kids

from random import randint
import time

# Make sure your green entries are sorted low to high or you'll never get a match
MY_TICKET = {"green": [13, 36, 43, 61, 69], "red": 18}

drawing = 0
start_time = time.time()
match = False
while not match:
    power_balls = {}
    white_drawing = []
    drawing += 1
    while len(white_drawing) <= 4:
        candidate = randint(1, 69)
        if candidate not in white_drawing:
            white_drawing.append(candidate)
    white_balls = sorted(white_drawing)
    power_balls["green"] = white_balls
    power_balls["red"] = randint(1, 26)

    if power_balls == MY_TICKET:
        print(f'We have a match! {power_balls} and it took {drawing} tries to get a win')
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print(f"It took {total_time} seconds to generate {drawing} tries")
        match = True

# Sample output 
# We have a match! {'green': [27, 28, 51, 68, 69], 'red': 22} and it took 231954286 tries to get a win
# It took 1015.89 seconds to generate 231954286 tries
