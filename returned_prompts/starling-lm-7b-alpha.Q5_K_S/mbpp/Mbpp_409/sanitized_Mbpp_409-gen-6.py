from typing import List, Tuple
def min_product_tuple(lst: List[Tuple[int, int]]) -> int:
    min_product = float("inf")
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            min_product = min(min_product, lst[i][0] * lst[i][1] * lst[j][0] * lst[j][1])
    return min_product