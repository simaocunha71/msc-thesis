from typing import List
def combinations_list(lst: List[str]) -> List[List[str]]:
    if len(lst) == 0:
        return [[]]
    result = []
    for i, x in enumerate(lst):
        rest = lst[i+1:]
        for c in combinations_list(rest):
            result.append([x] + c)
    return result