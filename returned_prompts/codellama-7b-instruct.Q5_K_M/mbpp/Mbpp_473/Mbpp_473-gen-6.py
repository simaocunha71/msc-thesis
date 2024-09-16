
from typing import List, Tuple

def tuple_intersection(tuple_list: List[Tuple[int, int]]) -> set:
    return set().union(*tuple_list)
