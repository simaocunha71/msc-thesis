from typing import List
def Diff(list1: List[int], list2: List[int]) -> List[int]:
    return [i for i in list1 if i not in list2] + [i for i in list2 if i not in list1]