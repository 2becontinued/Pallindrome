"""
Validates strings as palindromes.
"""

# Setup!

import string
from collections import deque
from collections import namedtuple
from collections import namedtuple

# Setup end!

def is_palindrome(value):  # Defines is_palindrome as a value
    if not isinstance(value, str):
        raise ValueError  # Raises a ValueError

    if value == "":
        return False

