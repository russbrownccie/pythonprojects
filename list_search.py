# List_search v0.1 - Russ Brown
# This program goes thru a list of 100k numbers, picks one at random, removes it from the list and keeps trying.
# I was interested in how many guesses and how long it would take to get the full 100k with the random generator
# future changes might include being able to input the range and being able to adjust all variables based on that number


import random,time
ourlist = []
count = 0
for i in range(1, 100000):
    ourlist.append(i)

tic = time.perf_counter()
while len(ourlist) > 0:
    my_number = random.randint(1, 100000)
    count += 1

    if my_number in ourlist:
        ourlist.remove(my_number)
        if len(ourlist) % 10000 == 0:
            print(f'{len(ourlist)/1000}% of the space left to search')
toc = time.perf_counter()
print(f"computation ran in {toc - tic:0.4f} seconds")
print(f'tried {count} guesses to get all of them')
