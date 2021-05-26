# This is a basic prime number test - Russ Brown 5/25/2021
# first it tests to see if a number is prime and if it finds a single factor returns the result "not prime"
# then the program asks if you want the factors and if so, factors and puts the results into an easy to read list
# The task is divided so that if it's a huge number, you can get a fast result before getting factors
# in addition you only have to search from 1 to the square root of the prime number
# any other number over the square root would have a factor below it.
# the checking function is improved by ruling out all even numbers as any even number divides by two
# for example, try 999999947 and 999999937 - timers are imported to see performance.
import time
import math

number = int(input("What is the number you want to test?: "))
is_it_prime = True
factor = []
second_factor = []

tic = time.perf_counter()

# first test looks to see if a number is prime and quits out the moment it finds it's not
if number % 2 != 0:
    for i in range(3, int(math.sqrt(number)+1), 2):
        if number % i == 0:
            is_it_prime = False
            break
else:
    is_it_prime = False
# if the number is prime
if is_it_prime:
    print("Prime")
    toc = time.perf_counter()
    print(f"computation ran in {toc - tic:0.4f} seconds")
# if not prime - do you want the factors - this is a bit longer more comprehensive search for all factors
else:
    print("Not Prime")
    want_factors = input("Would you like the factors?  Input y or n: ")
    if want_factors == "y":
        tic = time.perf_counter()
        for i in range(2, int(math.sqrt(number)+1)):
            if number % i == 0:
                alt_number = int(number / i)
                factor.append(i)
                second_factor.append(alt_number)
        second_factor.sort(reverse=False)
        all_factors = factor + second_factor
        print(all_factors)
        toc = time.perf_counter()
        print(f"computation ran in {toc - tic:0.4f} seconds")
    else:
        print("Affirmative - Good bye")
