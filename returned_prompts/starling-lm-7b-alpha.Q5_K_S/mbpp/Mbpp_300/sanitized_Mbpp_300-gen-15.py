import math
def count_binary_seq(n):
    # O(n) time and O(1) space
    if n == 0:
        return 1
    if n == 1:
        return 2
    return 4 * math.pow(2, n - 1)