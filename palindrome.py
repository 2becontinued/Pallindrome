"""
Validates strings as palindromes.
"""


def is_palindrome(value):  # Defines is_palindrome as a value
    if not isinstance(value, str):
        raise ValueError  # Raises a ValueError