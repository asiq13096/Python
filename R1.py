def new_list(number1, number2):
    return list(range(number1, number2))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

ran = new_list(num1, num2)

for i in ran:
    sum = ran[0] + i
    print(f"Current number {i}, Previous Number {ran[0]}, Sum {sum}")
    ran[0] = i

print(f"Printing current and previous number sum between {num1} and {num2}")