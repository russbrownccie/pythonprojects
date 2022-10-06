#  Ringer.py - solves ringer programs in the pennypress puzzle books - not optimized - for my mom...
#  Basically you have 5 wheels with 4 letters each - in theory, you dial each wheel left or right till you have 4 words
#  This program searchs all possible combos for the next 4 rings and sees if we match in a dictionary
#  Uses the load_dictonary file from impractical python projects to create a list of words to search through
#  Probably won't use this one too much

#  creates the word dictionary
import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')

# creates the list of numbers from 0000-3333 (with just those 4 digits) - this is our seed we rotate into the "wheels
# it would look like ["0000", "0001", "0002", "0003", "0010", "0011"] etc...only actually 256 entries

number_list = []

for second_number in range(4):
    for third_number in range(4):
        for fourth_number in range(4):
            for fifth_number in range(4):
                number_list.append(str(second_number) + str(third_number) + str(fourth_number) + str(fifth_number))


# - create the rings - all rings are double the length, so we can just add to 4 instead of wrapping back to 0
first_ring = "zsbmzsbm"
second_ring = "raepraep"
third_ring = "ubioubio"
fourth_ring = "civrcivr"
fifth_ring = "leayleay"

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
