# Simple Python Program with Arithmetic Operations

# Prompt user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Check if the second number is not zero before performing division
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "Cannot divide by zero."

# Display the results
print(f"\nResults for {num1} and {num2}:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")
