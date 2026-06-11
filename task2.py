import csv
import os

FILE_NAME = "expenses.csv"

def add_expense():
    desc = input("Enter expense description: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([desc, amount])

    print("Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    print("\n--- Expense List ---")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Item: {row[0]}, Amount: ₹{row[1]}")
    print()

def total_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            total += float(row[1])

    print(f"\nTotal Expenses: ₹{total}\n")

while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.\n")