#let users add income/expenses, categorize them, and display monthly summaries with charts
#file I/O, CSV handling, plotting, OOP

# fresh imports
import matplotlib.pyplot as plt
import csv

# add income
income = input('What was your income this month? ')
# add expenses
expenses = input('Add your expenses, separated by a comma: ').split(',')
# print expenses
print('Your expenses: ' + str(expenses))
# for each expense in expenses, print 'how would you like to categorize this expense and add it to a variable
expenses_categorizations = {}
money_left = float(income)
for expense in expenses:
  amount = float(expense.strip())
  categorization = input('How would you like to categorize this expense: ' + expense + ' ')
  if categorization in expenses_categorizations:
      expenses_categorizations[categorization] += amount
  else:
      expenses_categorizations[categorization] = amount
  money_left -= amount
print(expenses_categorizations)
#plot the data
plt.bar(expenses_categorizations.keys(), expenses_categorizations.values())
plt.title('Money Spent by Expense')
plt.xlabel('Expense Category')
plt.ylabel('Money Spent')
plt.show()
print(money_left)
