"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
from typing import Any, Callable, List, Optional, Union
import re as _re


def check(s: str) -> bool:  # noqa: T003
    """Check if the string is a vowel or not.

    :param s: A string to check whether it is starting with vowels or not.
    """
    return _re.match("^[aeiou]", s).group() is None  # noqa: T004,T005


def check_str(s: str) -> bool:
    """Check if the string is a vowel or not.

    :param s: A string to check whether it is starting with vowels or not.
    """
    return check(s)  # noqa: T004,T005
