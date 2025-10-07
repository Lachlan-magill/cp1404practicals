"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    classes_information = load_data(FILENAME)
    print(classes_information)
    display_data(classes_information)


def display_data(data):
    for subjects in data:
        subject_number = subjects[0]
        lecturer_name = subjects[1]
        number_of_students = subjects[2]
        print(f"{subject_number} is taught by {lecturer_name} and has {number_of_students} students")


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    all_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        all_data.append(parts)
    input_file.close()
    return all_data


main()