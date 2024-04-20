"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""
from typing import Optional, List

def replace_spaces(string: str):
    """
    :param str string: A string to check for white spaces and replace.
    :return: Returns a string without whitespaces or underscores.
    """
    return ''.join((x if x == '' else x.lower()) for x in string.split(' '))

def test_replace_spaces(replace_spaces):
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
