numbers = [3,1,4,1,5,9,2]
numbers[0]
#3
numbers[-1]
#2
numbers[3]
#1
numbers[:-1]
# all numbers but 2
numbers[3:4]
#1, 5
5 in numbers
#true
7 in numbers
#false
"3" in numbers
#false
numbers + [6, 5, 3]
# Added to the end of numbers

numbers[0] = 'ten'
numbers[-1] = 1
print(numbers)
print(numbers[2:])
print(9 in numbers)