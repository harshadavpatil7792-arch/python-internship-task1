import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount", "Category", "Date"])


# Add Expense
def add_expense():
    desc = input("Enter Expense Description: ")
    amount = float(input("Enter Amount: "))
    category = input("Enter Category (Food/Travel/Shopping/etc): ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([desc, amount, category, date])

    print("\nExpense Added Successfully!\n")


# View All Expenses
def view_expenses():
    print("\n------ All Expenses ------")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            # Skip header
            if row and row[0] == "Description":
                continue

            # Skip incomplete rows
            if len(row) < 4:
                continue

            print(f"Description : {row[0]}")
            print(f"Amount      : ₹{row[1]}")
            print(f"Category    : {row[2]}")
            print(f"Date        : {row[3]}")
            print("-" * 30)


# Search By Category
def search_category():
    category = input("Enter Category to Search: ").strip().lower()

    print(f"\nExpenses in '{category.title()}' Category\n")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row and row[0] == "Description":
                continue

            if len(row) < 4:
                continue

            if row[2].strip().lower() == category:
                found = True
                print(f"{row[0]} | ₹{row[1]} | {row[2]} | {row[3]}")

    if not found:
        print("No matching records found.")


# Total Per Category
def total_per_category():
    totals = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row and row[0] == "Description":
                continue

            if len(row) < 4:
                continue

            category = row[2]
            amount = float(row[1])

            totals[category] = totals.get(category, 0) + amount

    print("\n------ Category Wise Total ------")

    if totals:
        for cat, total in totals.items():
            print(f"{cat} : ₹{total:.2f}")
    else:
        print("No expenses found.")


# Monthly Total
def monthly_total():
    month = input("Enter Month (YYYY-MM): ")

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row and row[0] == "Description":
                continue

            if len(row) < 4:
                continue

            if row[3].startswith(month):
                total += float(row[1])

    print(f"\nTotal Spending in {month} : ₹{total:.2f}")


# Menu
def menu():

    create_file()

    while True:

        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Category Wise Total")
        print("5. Monthly Total")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_category()

        elif choice == "4":
            total_per_category()

        elif choice == "5":
            monthly_total()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


menu()