from typing import List, Callable
def is_polite(n: int) -> bool:
    if not n:
        return False
    if str(n).count('0') >= 1:
        return False
    if str(n).count('5') >= 1:
        return False
    if str(n).count('9') >= 1:
        return False
    return True