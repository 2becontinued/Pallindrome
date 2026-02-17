"""
Tests the palindrome module
"""
# Setup!

import pytest
from palindrome import is_palindrome

#Setup end!

def test_raises_a_ValueError_when_input_is_not_a_String(): # Defines a test.
    with pytest.raises(ValueError):
            is_palindrome(112)