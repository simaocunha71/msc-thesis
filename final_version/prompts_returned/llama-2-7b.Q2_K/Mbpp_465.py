"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""
from typing import Optional, Dict

def drop_empty(d:Optional[Dict]=None) -> Optional[Dict]:
    if not d: return None

    return {k:v for k,v in d.items() if v is not None}