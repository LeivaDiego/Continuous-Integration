import pytest
from mathlib import square, factorial, is_prime, gcd, lcm

# ===== BASIC MATH FUNCTION TESTS =====

# --- Test cases for square function ---
# Happy path tests
@pytest.mark.parametrize("n, expected", [
    (2, 4), # Positive integer
    (-3, 9), # Negative integer
    (1.5, 2.25), # Positive float
])
def test_square_happy_path(n, expected):
    assert square(n) == expected

# Edge/Error cases
@pytest.mark.parametrize("bad", [
    "a", # Non-numeric input
    None, # None input
    True, # Boolean input
])
def test_square_edge_cases(bad):
    with pytest.raises(TypeError):
        square(bad)