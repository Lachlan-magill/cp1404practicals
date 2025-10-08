import random

#Min, max and numbers in each line
numbers_per_line = 6
min = 1
max = 45


number_of_lines = int(input("How many quick picks? "))
while number_of_lines < 0:
    print("Need to be a real number!")
    number_of_lines = int(input("How many quick picks? "))
for i in range(number_of_lines):
    quick_picks = []
    for j in range(numbers_per_line):
        number = random.randint(min, max)
        while number in quick_picks:
            number = random.randint(min, max)
        quick_picks.append(number)
    quick_picks.sort()
    print(" ".join(f"{number:2}" for number in quick_picks))