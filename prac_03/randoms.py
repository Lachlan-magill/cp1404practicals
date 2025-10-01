import random

# Line 1: randint(5, 20)
# What did you see on line 1?
# I saw various numbers
# What was the smallest number you could have seen? 5
# What was the largest? 20

# Line 2: randrange(3, 10, 2)
# What did you see on line 2?
# I saw values go up in 2, like 3, 5, 7, 9
# What was the smallest number you could have seen? 3
# What was the largest? 9
# Could line 2 have produced a 4? No, because the step is 2, so only odd numbers starting from 3 are included.

# Line 3: uniform(2.5, 5.5)
# What did you see on line 3?
# I saw floating-point numbers like 3.1, 4.8, 2.6
# What was the smallest number you could have seen? 2.5
# What was the largest? 5.5

# Code to produce a random number between 1 and 100 inclusive:
random_number = random.randint(1, 100)
print(random_number)
