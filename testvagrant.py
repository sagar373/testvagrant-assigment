class HouseholdExpenses:
    def __init__(self):
        self.expense_categories = []
        self.weekly_budget = []

    def add_category(self, category):
        self.expense_categories.append(category)

    def add_weekly_budget(self, budget):
        self.weekly_budget.append(budget)

    def get_expense_categories(self):
        return self.expense_categories

    def get_weekly_budget(self):
        return self.weekly_budget

    def calculate_total_expenses(self):
        total_expenses = 0
        for category in self.expense_categories:
            total_expenses += category[1]
        return total_expenses

    def calculate_weekly_budget(self):
        total_budget = 0
        for budget in self.weekly_budget:
            total_budget += budget[1]
        return total_budget

# Create a new instance of the HouseholdExpenses class
household_expenses = HouseholdExpenses()

# Add expense categories
household_expenses.add_category(["Food", 100])
household_expenses.add_category(["Utilities", 50])
household_expenses.add_category(["Entertainment", 25])

# Add weekly budget
household_expenses.add_weekly_budget(["Food", 200])
household_expenses.add_weekly_budget(["Utilities", 100])
household_expenses.add_weekly_budget(["Entertainment", 50])

# Calculate total expenses and weekly budget
total_expenses = household_expenses.calculate_total_expenses()
weekly_budget = household_expenses.calculate_weekly_budget()

# Print results
print("Total Expenses:", total_expenses)
print("Weekly Budget:", weekly_budget)