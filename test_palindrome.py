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

def test_returns_False_when_empty_string_called():
    assert is_palindrome("") is False

def test_Returns_True_when_string_is_A():
    assert is_palindrome("a") is True

def test_Returns_False_when_string_is_Abc():
    assert is_palindrome("abc") is False

def test_Returns_True_when_string_is_Laval():
    assert is_palindrome("laval") is True

def test_Returns_False_when_string_is_Toronto():
    assert is_palindrome("toronto") is False

def test_Returns_True_when_string_is_Able_Was_I_ere_I_Saw_Elba():
    assert is_palindrome("ablewasiereisawelba") is True