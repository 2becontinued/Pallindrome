"""
Validates strings as palindromes.
"""

# Setup!

from collections import deque

# Setup end!

def is_palindrome(value):  # Defines is_palindrome as a value
    if not isinstance(value, str):
        raise ValueError  # Raises a ValueError


    prepared = "".join(ch.lower() for ch in value if ch.isalnum())  # Prepares the value variable for the algorithm

    if prepared == "":  # If the prepared string is nothing...
        return False  # Make it False.

    d = deque(prepared)  # D is the prepared variable converted as a deque

    while len(d) > 1:

        if d.popleft() != d.pop():  # If it's not a palindrome...
            return False  # Return False.

    return True  # If it IS a palindrome, return True