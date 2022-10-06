#  Ringer.py - solves ringer programs in the pennypress puzzle books - not optimized - for my mom...
#  Basically you have 5 wheels with 4 letters each - in theory, you dial each wheel left or right till you have 4 words
#  This program searches all possible combos for the next 4 rings and sees if we match in a dictionary
#  Uses the load_dictionary file from impractical python projects to create a list of words to search through
#  Probably won't use this one too much

# v 0.2 - does some dictionary optimization and streamlines the entry process so I just enter the rings in the beginning
# once for the program - if I was doing this all the time I'd input them in manually per run.



rings = ["zsbm", "raep", "ubio", "civr", "leay"]  # creates the input for the 5 rings outer to inner

import load_dictionary
# This set of operations creates the word list and takes the word list down from full entries to entries that are only
# 5 letters and match words that start with letters in the first ring and end with words that end in the last ring -

first_word_list = load_dictionary.load('2of4brif.txt')
second_word_list = [word for word in first_word_list if len(word) == 5]
third_word_list = [word for word in second_word_list if word[0] in rings[0]]
word_list = [word for word in third_word_list if word[4] in rings[4]]


# creates the list of numbers from 0000-3333 (with just those 4 digits) - this is our seed we rotate into the "wheels
# it would look like ["0000", "0001", "0002", "0003", "0010", "0011"] etc...only actually 256 entries

number_list = []

for second_number in range(4):
    for third_number in range(4):
        for fourth_number in range(4):
            for fifth_number in range(4):
                number_list.append(str(second_number) + str(third_number) + str(fourth_number) + str(fifth_number))


# - create the rings - all rings are double the length because they are repeated, so we can just add to 4 instead of wrapping back to 0
first_ring = rings[0]+rings[0]
second_ring = rings[1]+rings[1]
third_ring = rings[2]+rings[2]
fourth_ring = rings[3]+rings[3]
fifth_ring = rings[4]+rings[4]

#  - Create empty dictionary for final candidates to go into - it should only be one entry TBH
final_candidates = {}
# This part slices every wheel according to the number seed - if all 4 entries are in the word list,
# we write it to the final candidate dictionary

for number in number_list:
    first_word = first_ring[0] + second_ring[int(number[0])] + third_ring[int(number[1])] +\
                 fourth_ring[int(number[2])] + fifth_ring[int(number[3])]
    second_word = first_ring[1] + second_ring[int(number[0])+1] + third_ring[int(number[1])+1] +\
                  fourth_ring[int(number[2])+1] + fifth_ring[int(number[3])+1]
    third_word = first_ring[2] + second_ring[int(number[0])+2] + third_ring[int(number[1])+2] +\
                 fourth_ring[int(number[2])+2] + fifth_ring[int(number[3])+2]
    fourth_word = first_ring[3] + second_ring[int(number[0])+3] + third_ring[int(number[1])+3] +\
                  fourth_ring[int(number[2])+3] + fifth_ring[int(number[3])+3]
    if first_word in word_list and second_word in word_list and third_word in word_list and fourth_word in word_list:

        final_candidates[number] = [first_word, second_word, third_word, fourth_word]

print(final_candidates)
