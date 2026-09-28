def amount_to_return():
    total_bill = float(input("Enter the total bill amount: "))
    amount_paid = float(input("Enter the amount paid: "))
    change = amount_paid - total_bill
    return change

returned_amount = amount_to_return()
print("The shopkeeper should return:", returned_amount, "$")

