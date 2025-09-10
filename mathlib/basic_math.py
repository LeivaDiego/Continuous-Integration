from typing import Union

# Type alias for numbers (int and float)
Number = Union[int, float]


def square(n: Number) -> Number:
    """
    Returns the square of a number.
    Args:
        n (Number): The number to be squared.
    Returns:
        Number: The square of the input number.
    Raises:
        TypeError: If the input is not a number (int or float).
    """
    # Ensure the input is a number
    if not isinstance(n, (int, float)):
        raise TypeError(f"[ERROR] square(n) expects a number (int or float), Got: {type(n)}")

    # Return the squared value
    return n * n


def factorial():
    # TODO: Implement the factorial function
    pass

def is_prime():
    # TODO: Implement the is_prime function
    pass

def gcd():
    # TODO: Implement the gcd function
    pass

def lcm():
    # TODO: Implement the lcm function
    pass