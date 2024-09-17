from typing import List
import sys
def count_binary_seq(n: int) -> int:
    if n == 0:
        return 1
    return count_binary_seq(n-1) * 2