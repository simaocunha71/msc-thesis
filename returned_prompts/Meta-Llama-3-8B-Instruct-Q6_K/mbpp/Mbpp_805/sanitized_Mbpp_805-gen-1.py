from typing import List
def max_sum_list(list_of_lists: List[List[int]]) -> List[int]:
    return max(list_of_lists, key=sum)  # or: return max((sum(sublist), sublist) for sublist in list_of_lists)[1]  # Python 3.6+