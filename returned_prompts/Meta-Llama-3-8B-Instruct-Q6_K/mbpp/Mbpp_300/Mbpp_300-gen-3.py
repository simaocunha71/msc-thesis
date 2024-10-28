```
import math

def count_binary_seq(n):
    return math.comb(2*n, n)
```


The problem is asking to find the count of all binary sequences of length 2n such that the sum of the first n bits is the same as the sum of the last n bits.

The key observation here is that the sum of the first n bits and the sum of the last n bits will be the same only if the sequence is symmetric. In other words, the sequence will be of the form "011...1" or "110...0".

The number of binary sequences of length 2n can be calculated using the combination formula: `math.comb(2*n, n)`. This is because there are `2*n` choices for the first bit, and `n` choices for each of the remaining bits.

The unit test `assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)` helps to clarify the problem by showing that the expected output is `2.0` for `n=1`, which corresponds to the two symmetric sequences "00" and "11". The `math.isclose` function is used to account for floating point precision errors.

Here is the solution:
```
import math

def count_binary_seq(n):
    return math.comb(2*n, n)
```


This function takes an integer `n` as input and returns the count of all binary sequences of length `2n` such that the sum of the first `n` bits is the same as the sum of the last `n` bits. The function uses the `math.comb` function to calculate the number of combinations of `2*n` items taken `n` at a time, which corresponds to the number of symmetric binary sequences of length `2n`. The result is returned as an integer.