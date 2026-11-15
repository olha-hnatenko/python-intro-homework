import os
import csv
from datetime import datetime
print(os.getcwd())
if not os.path.exists("../data/expenses.csv"):
    print("expenses.csv not found.")
    raise SystemExit
else:
    print("expenses.csv found.")

with open("../data/expenses.csv", "r") as file:
    reader=csv.DictReader(file)
    expenses = list(reader)

food_expenses =[] 
for expense in expenses:
    expense['amount'] = float(expense['amount'])
    print(f"${expense['amount']:.2f}") 
    if expense['category'] == 'Food':
        print(f"Food expense: ${expense['amount']:.2f}")
        food_expenses.append(expense)
print(f"Total food expenses: ${sum(expense['amount'] for expense in food_expenses):.2f}")

now = datetime.now()
report_date=now.strftime("%B %d, %Y")
with open("food_report.txt", "w") as report:
    report.write(f"Food Expense Report - generated {report_date}\n")
    for expense in food_expenses:
        report.write(f"{expense['date']}: ${expense['amount']:.2f}\n")
    report.write(f"Total: ${sum(expense['amount'] for expense in food_expenses):.2f}\n")