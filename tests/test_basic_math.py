import pytest
from mathlib import square, factorial, is_prime, gcd, lcm

# ===== BASIC MATH FUNCTION TESTS =====

# ---------------------------------------
# Test cases for square function 
# ---------------------------------------
# Happy path tests
@pytest.mark.parametrize("n, expected", [
    (2, 4), # Positive integer
    (-3, 9), # Negative integer
    (1.5, 2.25), # Positive float
])
def test_square_happy(n, expected):
    assert square(n) == expected

# Edge/Error cases
@pytest.mark.parametrize("bad", [
    "a", # Non-numeric input
    None, # None input
    True, # Boolean input
])
def test_square_errors(bad):
    with pytest.raises(TypeError):
        square(bad)

# ---------------------------------------
# Test cases for factorial function
# ---------------------------------------
# Happy path tests
@pytest.mark.parametrize("n, expected", [
    (5, 120), # Positive integer
    (0, 1), # Zero
])
def test_factorial_happy(n, expected):
    assert factorial(n) == expected

# Edge/Error cases
# Type errors
@pytest.mark.parametrize("bad", [
    "a", # Non-integer string
    None, # None input
    True, # Boolean input
])
def test_factorial_type_errors(bad):
    with pytest.raises(TypeError):
        factorial(bad)

# Value errors
@pytest.mark.parametrize("bad", [
    -1, # Negative integer
    -5, # Another negative integer
])
def test_factorial_value_errors(bad):
    with pytest.raises(ValueError):
        factorial(bad)

# ---------------------------------------
# Test cases for is_prime function
# ---------------------------------------
# Happy path tests
@pytest.mark.parametrize("n, expected", [
    (2, True), # Smallest prime
    (3, True), # Small prime
    (4, False), # Small non-prime
    (17, True), # Larger prime
    (18, False), # Larger non-prime
])
def test_is_prime_happy(n, expected):
    assert is_prime(n) == expected

# Edge/Error cases
# Type errors
@pytest.mark.parametrize("bad", [
    "a", # Non-integer string
    None, # None input
    True, # Boolean input
])
def test_is_prime_type_errors(bad):
    with pytest.raises(TypeError):
        is_prime(bad)
# Edge cases for numbers less than 2
@pytest.mark.parametrize("n, expected", [
    (0, False), # Zero
    (1, False), # One
    (-5, False), # Negative integer
])
def test_is_prime_edge_cases(n, expected):
    assert is_prime(n) == expected