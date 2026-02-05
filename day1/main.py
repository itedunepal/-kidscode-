# Simple Python Program - Greeting and Calculator

def greet(name):
    """Function to greet a user"""
    return f"Hello, {name}!"

def add(a, b):
    """Function to add two numbers"""
    return a + b

# Main program
if __name__ == "__main__":
    # Get user input
    user_name = input("Enter your name: ")
    print(greet(user_name))
    
    # Simple calculation
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
