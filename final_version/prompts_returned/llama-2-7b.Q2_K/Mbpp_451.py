"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""
from typing import Any, Dict, List, Optional, Set, Type, Union  # noqa: F401
from copy import deepcopy  # noqa: F401
# Add your code here...


def remove_whitespaces(text: str) -> str:
    """Remove whitespaces from a given string.
    Args:
        text (str): The given string to modify.
    Returns:
        (str): A string without any whitespace characters.
    """
    # write your code here...
    return ''.join([i for i in text if i and not i.isspace()])
