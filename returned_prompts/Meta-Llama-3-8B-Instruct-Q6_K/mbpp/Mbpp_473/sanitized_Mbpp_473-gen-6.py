from typing import Tuple, List
from collections import Counter
def tuple_intersection(tuples1: List[Tuple], tuples2: List[Tuple]) -> List[Tuple]:
    counter1 = Counter(tuple(sorted(t)) for t in tuples1)
    counter2 = Counter(tuple(sorted(t)) for t in tuples2)
    return [t for t in counter1 & counter2]  # Get the intersection of two sets