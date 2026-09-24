from functools import reduce


def get_expenses():
    """
    Description:
    Gets monthly expense information from the user.

    Parameters:
    None

    Variables:
    expenses - list that stores the expense type and amount
    expense_type - name of the expense entered by the user
    amount - dollar amount of the expense

    Return:
    expenses - list of all expenses entered by the user
    """

    expenses = []

    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")

        if expense_type.lower() == "done":
            break

        try:
            amount = float(input("Enter the amount of the expense: $"))

            if amount < 0:
                print("Please enter a positive amount.")
            else:
                expenses.append((expense_type, amount))

        except ValueError:
            print("Please enter a valid number.")

    return expenses


def calculate_expenses(expenses):
    """
    Description:
    Uses reduce to calculate the total expense and find the
    highest and lowest expenses.

    Parameters:
    expenses - list containing the expense types and amounts

    Variables:
    total_expense - total amount of all expenses
    highest_expense - expense with the highest amount
    lowest_expense - expense with the lowest amount

    Return:
    total_expense, highest_expense, lowest_expense
    """

    total_expense = reduce(
        lambda total, expense: total + expense[1],
        expenses,
        0
    )

    highest_expense = reduce(
        lambda highest, expense:
        expense if expense[1] > highest[1] else highest,
        expenses
    )

    lowest_expense = reduce(
        lambda lowest, expense:
        expense if expense[1] < lowest[1] else lowest,
        expenses
    )

    return total_expense, highest_expense, lowest_expense


def main():
    """
    Description:
    Runs the monthly expense program and displays the results.

    Parameters:
    None

    Variables:
    expenses - list returned from get_expenses
    total_expense - total amount of all expenses
    highest_expense - expense with the highest amount
    lowest_expense - expense with the lowest amount

    Return:
    None
    """

    print("Monthly Expense Analyzer")
    print("------------------------")

    expenses = get_expenses()

    if len(expenses) == 0:
        print("No expenses were entered.")
        return

    total_expense, highest_expense, lowest_expense = calculate_expenses(expenses)

    print("\nMonthly Expense Summary")
    print("-----------------------")
    print(f"Total expenses: ${total_expense:.2f}")
    print(f"Highest expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")


if __name__ == "__main__":
    main()