

# Powerball Lottery Simulator - v 0.3
# Written by Russ Brown for Python Crash Course project
# This program attempts to continuously draw for powerball until it gets a match on the MY_TICKET variable
# Powerball draws 5 numbers from a pool of white balls 1-69 and one red ball 1-26
# This program saves those as a dictionary, and then loops.   When the entire drawing is done, it compares tickets
# The program will tell you how long it took and how many tries - 400 million tries could take up to an hour on mine
# Written totally for fun - gambling is bad, kids

# v 0.3 - added Selenium webscraping to get the last powerball numbers drawn from the website - you have to configure
# your own selenium drivers and driver paths - this is for my machine
# Also added a printout to console every 10 mil tries just to remind me it was still running


from random import randint
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "/home/john/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

URL = "https://www.powerball.com"

driver.get(URL)
numbers = driver.find_element(By.CLASS_NAME, "field_numbers")
date = driver.find_element(By.CLASS_NAME, "field_draw_date")

drawing_date = date.text

# The next lines take the scrapped data and convert it to integers in a list and populate the dictionary with it
powerball = numbers.text
formatted = powerball.replace('\n', ' ')
stringlist = (formatted.split())
finallist = [int(item) for item in stringlist]
driver.close()
green_list = finallist[0:5]
redball = finallist[5]


print(drawing_date)
MY_TICKET = {"green": green_list, "red": redball}
print (MY_TICKET)


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

    if drawing % 10000000 == 0:
        print(f"{drawing}, {power_balls}")

    if power_balls == MY_TICKET:
        print(f'We have a match! {power_balls} and it took {drawing} tries to get a win')
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print(f"It took {total_time} seconds to generate {drawing} tries")
        match = True

# Sample output
# We have a match! {'green': [27, 28, 51, 68, 69], 'red': 22} and it took 231954286 tries to get a win
# It took 1015.89 seconds to generate 231954286 tries
