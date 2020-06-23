""" credit_condition = input("If True press 1: ")
if 1 == int(credit_condition):
    print("Down-payment: " + str((1000000 * 10) / 100))
else:
    print("Down-payment: " + str((1000000 * 20) / 100))
"""

price = 1000000
credit_condition = input("Enter anything if credit condition is good: ")
if credit_condition:
    print("Down-payment: " + str((1000000 * 20) / 100))
else:
    print("Down-payment: " + str((1000000 * 10) / 100))