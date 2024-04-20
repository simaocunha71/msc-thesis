"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""
from typing import Any, Dict, List, Optional


def merge_dictionaries(*dictionaries: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    assert all([isinstance(d1, dict) for d1 in dictionaries])
    return {k: v for k, v in max(dictionaries, key=len)})
