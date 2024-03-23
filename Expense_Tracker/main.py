from ExpenseTracker import expense_tracker
tracker = expense_tracker()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. View Expense Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")
    #print("\n")
    if choice == "1":
        date = input("Enter expense date (YYYY-MM-DD): ")
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        tracker.add_expense(date, category, amount)
        print("Expense added successfully.")
    elif choice == "2":
        print("All Expenses:")
        tracker.view_all_expenses()
    elif choice == "3":
        index = int(input("Enter expense index to edit: "))
        date = input("Enter new expense date (YYYY-MM-DD): ")
        category = input("Enter new expense category: ")
        amount = float(input("Enter new expense amount: "))
        tracker.edit_expense(index, date, category, amount)
    elif choice == "4":
        index = int(input("Enter expense index to delete: "))
        tracker.delete_expense(index)
    elif choice == "5":
        print("Expense Summary:")
        summary = tracker.get_expense_summary()
        for category, total in summary.items():
            print(f"{category}: ${total}")
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")