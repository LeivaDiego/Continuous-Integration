def square(n: int | float) -> int | float:
    """
    Calculate the square of a number.
    Args:
        n (int | float): The number to be squared.
    Returns:
        int | float: The square of the input number.
    Raises:
        TypeError: If the input is not a number (int or float).
    """
    # Ensure the input is a number
    if not isinstance(n, (int, float)):
        raise TypeError(f"[ERROR] square(n) expects a number (int or float), Got: {type(n)}")
    
    # Return the squared value
    return n * n


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    Args:
        n (int): The non-negative integer to calculate the factorial for.
    Returns:
        int: The factorial of the input integer.
    Raises:
        TypeError: If the input is not a non-negative integer.
    """
    # Ensure the input is a non-negative integer
    if not isinstance(n, int):
        raise TypeError(f"[ERROR] factorial(n) expects an integer, Got: {type(n)}")
    if n < 0:
        raise TypeError("[ERROR] factorial(n) expects a non-negative integer")
    
    # Calculate the base cases (0! = 1 and 1! = 1)
    if n == 0 or n == 1:
        return 1
    # Calculate the factorial recursively
    else:
        return n * factorial(n - 1)


def is_prime():
    # TODO: Implement the is_prime function
    pass

def gcd():
    # TODO: Implement the gcd function
    pass

def lcm():
    # TODO: Implement the lcm function
    pass