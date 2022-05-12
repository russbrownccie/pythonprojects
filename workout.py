# Workout (Expressway) tracker - Russ Brown - v0.1
# This is a start at making a tracker for my Expressway workouts - (one set, 12 reps, 2 sec extend, 4 sec contract)
# this pulls the workouts and my weights from a file called workouts.txt
# The file is in dictionary format - more exercise can be added as one wishes
# The idea is you do 12 reps in one set 
# If you succeed in doing 12 reps, all the weights are bumped up by 5 lbs (should be 5% but the machines are in lbs)
# If you struggled, it will ask which exercises (must type the exact exercise but it will convert to title for you)
# It will then ask you want to do the same weight again next time, or take it down a step
# Future modifications might include taking the input as soon as the exercise is done (assuming done in order)
# Some input validation - maybe track each exercise as you go and then you won't forget
# Afterwards, it will write back to workouts.txt with the new values
# I run this in replit so I just browse to the replit and start running it while I do my workout
# Feel free to use for your own benefit

import ast  # needed to convert the str to dict when pulled from workouts.txt
# open workout and convert to a dictionary
with open("workouts.txt") as file:
    data = file.read()

workout = ast.literal_eval(data)
# print out the current workout for this session
print('For This Workout:\n\n')
for k, v in workout.items():
    print(k + ' -- weight ' + str(v))
# ask if all workouts were completed successfully
success = input("\n\nWere you able to do all the reps in all exercises?: (y/n) ").lower()
if success == 'y':
    next_workout = {k: (v+5) for k, v in workout.items()}  # bumps all workouts up by 5
    print('Good job')
# if workouts not completed successfully - ask which ones and ask if I want same weight next time or go down a step
else:
    next_workout = {k: (v+5) for k, v in workout.items()}  # bumps all workouts up by 5 - then changes bad ones
    missed_exercises = True
    while missed_exercises == True:
        not_success = input('Which exercises did you struggle with? - type e to exit: ').title()
        if not_success in next_workout:
            same_next_time = input('Do you want to try same workout next time(y) or go down a step(n)')
            if same_next_time == 'y':
                next_workout[not_success] -= 5  # try same workout next time
            else:
                next_workout[not_success] -= 10  # take a step back for the next workout
        else:
            missed_exercises = False

# finally - write the new dictionary to the workouts.txt and overwrite the old value with new dict
with open('workouts.txt', 'w') as file:
    file.write(str(next_workout))
