"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""
from typing import Any, Dict

def drop_empty(dictionary:Dict[Any,Any]) -> Dict[Any,Any]:
    ret = {}
    for (key,value) in dictionary.items():
        if value is None or not value:
            continue
        
        ret[key] = value
    return ret