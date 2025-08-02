# Basic Calculator Program

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to input a mathematical operation
operation = input("Enter an operation (+, -, *, /): ")

# Perform the operation based on user's input
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
#output 
''' 
Enter the first number: 10  
Enter the second number: 5  
Enter an operation (+, -, *, /): +  
10.0 + 5.0 = 15.0
'''