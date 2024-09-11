from typing import List, Tuple
def min_k(list_tuple, k):
    return sorted(list_tuple, key=lambda item: item[1])[:k]