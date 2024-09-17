from typing import List, Tuple
def add_lists(list1: List[int], tuple1: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple1 + tuple(list1)