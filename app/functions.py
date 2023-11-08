def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Args:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    result = a + b
    return result

def subtract_numbers(a, b):
    """
    Subtracts the second number from the first and returns the result.

    Args:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The difference between the two numbers.
    """
    result = a - b
    return result

def divide_numbers(a, b):
    """
    Divides the first number by the second and returns the result. Handles division by zero.

    Args:
    a (int or float): The numerator (dividend).
    b (int or float): The denominator (divisor).

    Returns:
    int or float: The result of the division.
    """
    if b == 0:
        return "Division by zero is not allowed"
    result = a / b
    return result

def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.

    Args:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The result of multiplying the two numbers.
    """
    result = a * b
    return result
