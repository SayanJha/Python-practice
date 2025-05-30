# Basic Calculator with error handling input validation
def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """A simple attempt to implement try-except block"""
    try:
        result = x / y 
    except ZeroDivisionError:
        return f"Cannot divide {x} by {y}!"
    else:
        return result
    
def main():
    while True:
        print("""
Select operation: 
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
""")  # The outer while loop keeps the code running until the user enters 5
      # to quit.
      # The inner while loop keeps asking the user to enter a valid number
        while True:
            try:
                choice = float(input("Enter choice (1/2/3/4/5): "))
                if choice in (1, 2, 3, 4, 5): # It's a tuple
                    break
                else:
                    print("Invalid operation. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if choice == 1:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            print(f"The sum of {num1} and {num2} is: {add(num1, num2)}")
        elif choice == 2:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            print(f"The difference between {num1} and {num2} "
                f"is: {subtract(num1, num2)}")
        elif choice == 3:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            print(f"The product of {num1} and {num2} is: {multiply(num1, num2)}")
        elif choice == 4:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            print(f"The result of dividing {num1} by {num2} "
                  f"is: {divide(num1, num2)}")
        elif choice == 5:
            print("Exiting the calculator...")
            break

if __name__ == "__main__": # Only run the main function if this file is
    main()                 # executed directly

