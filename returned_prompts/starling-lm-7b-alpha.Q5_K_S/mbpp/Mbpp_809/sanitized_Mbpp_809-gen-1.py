from typing import Tuple
def check_smaller(t1: Tuple, t2: Tuple) -> bool:
    if len(t1) != len(t2):
        return False

    for i, j in zip(t1, t2):
        if i > j:
            return False

    return True