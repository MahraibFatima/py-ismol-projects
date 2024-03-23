class expense_tracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, category, amount):
        self.expenses.append({"date": date, "category": category, "amount": amount})

    def view_all_expenses(self):
        for index, expense in enumerate(self.expenses):
            print(f"{index + 1}. {expense}")

    def edit_expense(self, index, date, category, amount):
        if 0 < index <= len(self.expenses):
            self.expenses[index - 1] = {"date": date, "category": category, "amount": amount}
        else:
            print("Invalid expense index.")

    def delete_expense(self, index):
        if 0 < index <= len(self.expenses):
            del self.expenses[index - 1]
        else:
            print("Invalid expense index.")

    def get_expense_summary(self):
        summary = {}
        for expense in self.expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount
        return summary