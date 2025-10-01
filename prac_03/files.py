
# Create file
FILENAME = "name.txt"
users_name = input("Enter your name: ")
out_file = open(FILENAME, 'w')
print(f"{users_name}", file=out_file)
out_file.close()

# Read File
read_file = open(FILENAME, 'r')
names = read_file.read()
print(f"Hi {names}")
read_file.close()

# Read the first two numbers and print their sum
with open("numbers.txt", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    result = number1 + number2
    print(result)

# Read all lines, convert to integers, and print the total
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)
