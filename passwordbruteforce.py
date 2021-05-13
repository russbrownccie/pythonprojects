# This is a very LOWGRADE password test tool to see if I can generate a random password and brute force tool
# this is very low grade and is used to test my programming especially since I like code breaking challenges
# runs best under a terminal window in linux - open term, type "python3 passwordbruteforce.py"
# will update as I learn more and figure out ways to optimize
# Version 1.0 - Russell Brown CCIE #57653 - 5/2/21
# On my current PC I cycle thru the lower case alphabet with 100% processor in about 50 sec as a benchmark

# first, let's generate a random 5 letter password

import random
nr_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

for alpha in range(5): 
  password.append(random.choice(nr_letters))

# This is an output of the final product as a string for testing but program will compare lists (faster than comparing joined strings)
final_password = ("".join(password))
print(f"The password will be {final_password}")

#sets up the initial bruteforce list

bruteforce = ["a", "a", "a", "a", "a" ]

#sets up the conditions to cycle thru the letters
#eventually want to input length as a number and automate this whole script in other for loops with ranges

doesnotmatch = True

while doesnotmatch:

        for fifth_letter in nr_letters:
          #This will print the first letter which only rotates after the entire keyspace as a marker of progress
          print(bruteforce[0])
          bruteforce[0] = fifth_letter
          for fourth_letter in nr_letters:
            bruteforce[1] = fourth_letter
            for third_letter in nr_letters:
              bruteforce[2] = third_letter
              for second_letter in nr_letters:
                bruteforce[3] = second_letter
                for first_letter in nr_letters:
                  bruteforce[4] = first_letter
                  if bruteforce == password:
                    doesnotmatch = False
                    print(f"password is {bruteforce}")
                    #want to find right break command here
                    exit()
