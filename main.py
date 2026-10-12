

def add_numbers(num1, num2):
    return num1 + num2
    
def subtract_numbers(num1, num2):
    return num1 - num2
    
def multiply_numbers(num1, num2):
    return num1 * num2
    
def divide_numbers(num1, num2):
    if num2 == 0:
        return str(input("Cannot divide by zero."))
    else: 
     return num1 / num2
    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nChoose Operation: ")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = int(input("\nChoose Operation: "))

if choice == 1:
    result = add_numbers(num1, num2)
    print(f"Result: {result}")
    
elif choice == 2:
    result = subtract_numbers(num1, num2)
    print(f"Result: {result}")

elif choice == 3:
    result = multiply_numbers(num1, num2)
    print(f"Result: {result}")

elif choice == 4:
    result = divide_numbers(num1, num2)
    print(f"Result: {result}")

else:
    print("Invalid operation choice.")
    
    


   
    

    
    
