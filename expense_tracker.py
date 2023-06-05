class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

class Category:
    def __init__(self):
        self.categories = {}

    def add_expense(self, category, amount):
        if not category in self.categories:
            self.categories[category] = []
        self.categories[category].append(Expense(category, amount))

    def total_expenses(self):
        total = 0
        for category, expenses in self.categories.items():
            for expense in expenses:
                total += expense.amount
        return total

    def total_expenses_by_category(self, category):
        total = 0
        if category in self.categories:
            for expense in self.categories[category]:
                total += expense.amount
        return total

    def show_summary(self):
        for category, expenses in self.categories.items():
            total = self.total_expenses_by_category(category)
            print(f"Category: {category} - Total Expenses: ${total:.2f}")


def main():
    my_expenses = Category()
    while True:
        print("\n1. Add an expense")
        print("2. Show total expenses")
        print("3. Show expenses by category")
        print("4. Show summary")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            category = input("Enter the category: ")
            amount = float(input("Enter the expense amount: "))
            my_expenses.add_expense(category, amount)
        elif choice == '2':
            total = my_expenses.total_expenses()
            print(f"Total expenses: ${total:.2f}")
        elif choice == '3':
            category = input("Enter the category: ")
            total = my_expenses.total_expenses_by_category(category)
            print(f"Total {category} expenses: ${total:.2f}")
        elif choice == '4':
            my_expenses.show_summary()
        elif choice == '5':
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
