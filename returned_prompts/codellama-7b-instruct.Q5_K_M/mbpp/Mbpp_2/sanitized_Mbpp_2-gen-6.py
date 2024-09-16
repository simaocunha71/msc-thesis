from typing import List, Set
def similar_elements(list1: List, list2: List) -> Set:
    return set(list1).intersection(set(list2))