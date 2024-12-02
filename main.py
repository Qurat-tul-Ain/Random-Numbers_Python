# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)
#--------------------------------------------------------------------------------

# METHOD 1

import random

# Constants
MIN_NUMBER: int = 1
MAX_NUMBER: int = 100
N_RANDOM_NUMBER: int = 10

# Initialize an empty list to store the random numbers
number_list = []

# Function: Using For Loop to generate random numbers
for i in range(N_RANDOM_NUMBER):  
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_list.append(random_number)
    print(random_number, end=" ")

# Print the entire list of generated random numbers
print("\nList of Random Numbers: ", number_list)



#method 2
# using numpy

MIN_NUMBER :int = 1
MAX_NUMBER :int = 101
N_RANDOM_NUMBER :int = 10

import numpy as np
                                                                   # samples
number_list = np.random.randint(MIN_NUMBER, MAX_NUMBER, N_RANDOM_NUMBER)
print(*number_list)