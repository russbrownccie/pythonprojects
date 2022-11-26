# This very simple program pulls from a list called records.txt numbering from 2 to 890
# This references a page from "1000 recordings to hear before you die" by Tom Moon
# You pick a recording at random based on the page - the start of an entry on that page is what you listen to
# If there are two entries on that page, you can say not to remove the entry from the list, so it can come up again
# Very little error checking on this - anything other than y won't delete the entry


# make a string list using the commented out code below - that will create the text file needed - 
# comment out after creating

# record_list = []
# for i in range(2, 891):
#     record_list.append(str(i))

# with open("records.txt", "w") as file:
#     for item in record_list:
#         file.write(f"{item}\n")

import random
record_list = []
with open("records.txt", "r") as file:
    data = file.readlines()
    for item in data:
        record_list.append(item)

remove_num = random.choice(record_list)
print(f"The page entry for today is {remove_num}")
choice = input("Do you wish to remove this page from the list - type y or n: ").lower()
if choice == "y":
    record_list.remove(remove_num)

with open("records.txt", "w") as file:
    for item in record_list:
        file.write(f"{item}")
