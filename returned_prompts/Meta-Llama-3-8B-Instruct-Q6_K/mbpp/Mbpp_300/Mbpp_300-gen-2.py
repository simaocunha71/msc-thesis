```
import math

def count_binary_seq(n):
    return math.comb(2**n, n)
```
The problem asks to find the count of all binary sequences of length 2n such that the sum of the first n bits is the same as the sum of the last n bits. This is equivalent to finding the number of binary sequences of length 2n where the first n bits are the same as the last n bits.

The problem can be solved using combinatorics. For each binary sequence of length 2n, we can select the first n bits independently of the last n bits. This is because the first n bits and the last n bits are independent of each other.

The number of ways to select the first n bits is 2^n, since there are 2^n possible combinations of n bits (0s and 1s).

The number of ways to select the last n bits is also 2^n, since it is independent of the first n bits.

The total number of binary sequences is the product of the number of ways to select the first n bits and the number of ways to select the last n bits, which is (2^n) * (2^n) = 2^(2n).

This is equivalent to the binomial coefficient "n choose 2n", which is calculated using the formula math.comb(2**n, n).

The unit test `assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)` checks if the function returns the correct count for n=1. The expected output is 2.0, which is the result of the formula math.comb(2**1, 1) = 2. The tolerance is set to 0.001 to account for floating point precision errors.