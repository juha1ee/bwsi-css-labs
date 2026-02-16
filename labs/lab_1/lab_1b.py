"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    else:
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")

def request_sanitized_number(prompt: str) -> float:
    """
    Function to request a sanitized number for the operation
    
    Returns:
        float: The sanitized numeric input by the user
    """
    while True:
        try: 
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def request_sanitized_operation(prompt: str) -> str:
    """
    Function to request a sanitized and valid operation

    Returns:
        str: The sanitized operation by the user
    """
    operation = input(prompt).strip().lower()
    while True:
        if ((operation != "add") and (operation != "subtract") and (operation != "multiply") and (operation!= "divide")):
            print("Invalid input. Please enter a valid operation.")
            operation = input(prompt).strip().lower()
        else:
            return operation

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = request_sanitized_number("Enter the first number: ")
    num2 = request_sanitized_number("Enter the second number: ")
    operation = request_sanitized_operation("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
