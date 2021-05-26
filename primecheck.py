# This is a basic prime number test - Russ Brown 5/25/2021
# first it tests to see if a number is prime and if it finds a single factor returns the result "not prime"
# then the program asks if you want the factors and if so, factors and puts the results into an easy to read list
# The task is divided so that if it's a huge number, you can get a fast result before getting factors
# in addition you only have to search from 2 to half the distance of the number
# any other number over half would have a factor in the first searched half
# for example, try 999999947 and 999999937 - timers are imported to see performance.
import time

number = int(input("What is the number you want to test?: "))
is_it_prime = True
factor = []

tic = time.perf_counter()
for i in range(2, int(number/2 + 1)):
# for i in range(2, number):
    if number % i == 0:
        is_it_prime = False
        break

if is_it_prime:
    print("Prime")
    toc = time.perf_counter()
    print(f"computation ran in {toc - tic:0.4f} seconds")

else:
    print("Not Prime")
    want_factors = input("Would you like the factors?  Input y or n: ")
    if want_factors == "y":
        tic = time.perf_counter()
        for i in range(2, int(number/2 + 1)):
            if number % i == 0:
                factor.append(i)

        print(factor)

        toc = time.perf_counter()
        print(f"computation ran in {toc - tic:0.4f} seconds")
    else:
        print("Affirmative - Good bye")
