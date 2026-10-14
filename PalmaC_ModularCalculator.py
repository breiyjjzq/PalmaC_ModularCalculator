
# Main functions
def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2
    
def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero."
    return num1 / num2


# Ask the user to enter two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Display the available operations
print("\nChoose Operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

# Ask the user to choose an operation
choice = input("\nChoose Operation: ")

# Perform the selected operation
if choice == "1":
    result = add_numbers(num1, num2)
elif choice == "2":
    result = subtract_numbers(num1, num2)
elif choice == "3":
    result = multiply_numbers(num1, num2)
elif choice == "4":
    result = divide_numbers(num1, num2)
else:
    result = "Invalid operation choice."

# Display the result
print("Result:", result)



    




    
    


   
    

    
    
