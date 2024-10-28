from collections import Counter
from typing import List
def max_occurrences(my_list: List) -> int:
    counter = Counter(my_list)
    return counter.most_common()[0][0]