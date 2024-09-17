from typing import List
def check_greater(arr: List[int], num: int) -> bool:
    for x in arr:
        if x > num:
            return False
    return True