
import math
def count_binary_seq(n):
    if n == 0:
        return 1
    else:
        return 2 ** n + count_binary_seq(n - 1)


