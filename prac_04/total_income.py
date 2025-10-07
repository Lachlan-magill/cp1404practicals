"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    total = calculate_total(incomes, months)
    print_reportt(incomes, months, total)


def print_reportt(incomes, months, total):
    for number_of_months in range(1, months + 1):
        income = incomes[number_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(number_of_months, income, total))


def calculate_total(incomes, months):
    for number_of_months in range(1, months + 1):
        income = float(input(f"Enter income for month {str(number_of_months)}: "))
        incomes.append(income)
    print("\nIncome Report\n-------------")
    total = 0
    return total


main()