"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""
from typing import Any, Dict, List, Optional, Tuple
from funcy import any_of, first, from_, map_, to

def Extract(lst: List[List]) -> List[Any]:
    def _Extract(lst: List) -> Any:
        return list(map(_Extract, lst)) if lst else None
    
    return _Extract(lst)
