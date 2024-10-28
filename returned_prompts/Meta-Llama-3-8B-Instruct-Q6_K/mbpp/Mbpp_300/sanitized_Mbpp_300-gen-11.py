import math
def count_binary_seq(n):
    def count_helper(k, n, count):
        if k == 0:
            return count
        return count_helper(k-1, n, count + (1 if k <= n else -1) * 2**(n-k))

    return count_helper(n, n, 0)