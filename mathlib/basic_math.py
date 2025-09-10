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
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative integer.
    """
    # Ensure the input is a non-negative integer
    if not isinstance(n, int):
        raise TypeError(f"[ERROR] factorial(n) expects an integer, Got: {type(n)}")
    if n < 0:
        raise ValueError("[ERROR] factorial(n) expects a non-negative integer")
    # Calculate the base cases (0! = 1 and 1! = 1)
    if n == 0 or n == 1:
        return 1
    # Calculate the factorial recursively
    else:
        return n * factorial(n - 1)

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    Args:
        n (int): The integer to check for primality.
    Returns:
        bool: True if the number is prime, False otherwise.
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative integer.
    """
    # Ensure the input is a positive integer
    if not isinstance(n, int):
        raise TypeError(f"[ERROR] is_prime(n) expects an integer, Got: {type(n)}")
    if n < 0:
        raise ValueError("[ERROR] is_prime(n) expects a positive integer")
    # Handle base cases
    if n == 0 or n == 1:
        # 0 and 1 are not prime numbers
        return False
    if n == 2:
        # 2 is the only even prime number
        return True
    # Check for divisibility by odd numbers from 3 up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2): # Increment by 2 to check only odd numbers
        if n % i == 0:
            # If a divisor is found, then n is not prime
            return False
    # If no divisors were found, then n is prime
    return True

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
    Args:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        int: The GCD of the two input integers.
    Raises:
        TypeError: If either input is not an integer.
    """
    # Ensure the inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"[ERROR] gcd(a, b) expects two integers, Got: {type(a)} and {type(b)}")
    # Get the absolute values of a and b
    a, b = abs(a), abs(b)
    # Loop until b becomes 0
    while b != 0:
        # Update a and b using the Euclidean algorithm
        # Swap a with b and b with the remainder of a divided by b
        a, b = b, a % b
    # When b is 0, a contains the GCD
    return a

def lcm(a: int, b: int) -> int:
    # Ensure the inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"[ERROR] lcm(a, b) expects two integers, Got: {type(a)} and {type(b)}")
    # Handle the base case where either a or b is 0
    if a == 0 or b == 0:
        return 0 # LCM is 0 if either number is 0
    # Calculate the LCM using the relationship between GCD and LCM
    return abs(a * b) // gcd(a, b)
