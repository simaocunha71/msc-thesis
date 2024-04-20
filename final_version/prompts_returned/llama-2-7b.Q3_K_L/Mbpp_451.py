"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""
from typing import Optional, List

def remove_whitespaces(word:str) -> str:
    """
    word = " Google    Flutter    "  # 1  2  3
    return = " GoogleFlutter"      # 1  2  3

    :param word: str to be modified

    :return: str with all whitespaces removed
    """
    word = ' '.join(word.split())
    return word
