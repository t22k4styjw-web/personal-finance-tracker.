
print("Personal Finance Tracker")

income = float(input("Enter your monthly income (£): "))
expenses = float(input("Enter your monthly expenses (£): "))

savings = income - expenses

if income > 0:
    savings_rate = (savings / income) * 100
else:
    savings_rate = 0

print("\n--- Financial Summary ---")
print("Monthly savings: £", round(savings, 2))
print("Savings rate:", round(savings_rate, 2), "%")

