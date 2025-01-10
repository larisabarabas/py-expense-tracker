# Build a simple expense tracker application to manage your finances. The application should allow users to add, delete, and view their expenses. The application should also provide a summary of the expenses.

# Requirements
# Application should run from the command line and should have the following features:

# Users can add an expense with a description and amount.
# Users can update an expense.
# Users can delete an expense.
# Users can view all expenses.
# Users can view a summary of all expenses.
# Users can view a summary of expenses for a specific month (of current year).
# Here are some additional features that you can add to the application:

# Add expense categories and allow users to filter expenses by category.
# Allow users to set a budget for each month and show a warning when the user exceeds the budget.
# Allow users to export expenses to a CSV file.

# Expense -> ID, Date, Description, Amount

import argparse
import os
import json
from datetime import date


def create_parser():
    parser = argparse.ArgumentParser(prog="expense-tracker",description="Expense tracker")
    subparser = parser.add_subparsers(dest="command")
    addParser = subparser.add_parser('add')

    addParser.add_argument("-d", "--description",type=str, metavar="", help="Add expense description")
    addParser.add_argument("-a", "--amount",type=int, metavar="", help="Add expense amount")

    summaryParser = subparser.add_parser("summary")
    summaryParser.add_argument("-m", "--month", type=int, metavar="", help="View all expenses for a specific month")

    subparser.add_parser("list")

    deleteParser = subparser.add_parser("delete")
    deleteParser.add_argument("-id", "--id",type=int, metavar="", help="Delete expense by id")
    
    subparser.add_parser("update")
   
    return parser


def add_expense(expense, amount):
    expenses = []
    today = str(date.today())

    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    expenses.append({"id": len(expenses) + 1, "description": expense, "amount": amount, "date":today })
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)
    print("Expense added successfully")

def list_expenses():
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
            
            print(f"# {'ID':<5} {'Date':<15} {'Description':<30} {'Amount'}")
            for index, expense in enumerate(expenses):
                print(f'#{expense['id']:<5} {expense['date']:<15} {expense['description']:<30} {expense['amount']}')
    else:
        print("There aren't any expenses so far")

def delete(id):
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
            if 0 < id <=len(expenses):
                for index, expense in enumerate(expenses):
                    if expense['id'] == id:
                        expenses.pop(index)
                        with open('expenses.json', 'w') as file:
                            json.dump(expenses, file)
                        print('Expense successfully deleted')
    
    else:
        print("No expense found to delete")


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete(args.id)
    elif args.command == "update":
        print(f'Here we update an expense: {int(args.update)}')
    elif args.command == "summary" and not args.month:
        print(f'Total summary ')
    elif args.command == "summary" and args.month:
        print(f'Summary for the specific month {args.month}')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()