    return pow(n, p - 2, p)  # pow(a, b, c) returns a^b % c
    # The modulo operation is performed in O(log p) time, much faster than the naive approach of repeated multiplication. This is because the binary representation of p-2 has a lot of trailing zeros, and we can take advantage of this to reduce the number of multiplications needed. The time complexity is therefore O(log p), which is much faster than the naive approach of O(p).


