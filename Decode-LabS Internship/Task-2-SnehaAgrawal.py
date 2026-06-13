spend_money = 0
print("Expense Tracker")
print("Enter 0 when you are done.\n")
while True:
    amount = float(input("Enter expense: "))
    if amount == 0:
        break
    spend_money = spend_money + amount

print("\nTotal Amount spent: ", spend_money)