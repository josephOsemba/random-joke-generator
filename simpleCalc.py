num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result: " + str(float(num1) + float(num2)))
elif operation == "-":
    print("Result: " + str(float(num1) - float(num2)))
elif operation == "*":
    print("Result: " + str(float(num1) * float(num2)))
elif operation == "/":
    print("Result: " + str(float(num1) / float(num2)))
else:
    print("Invalid operation. Please try again.")