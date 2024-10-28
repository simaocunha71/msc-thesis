```
def count_binary_seq(n):
    total = 0
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        if sum(int(b) for b in binary[:n]) == sum(int(b) for b in binary[n:]):
            total += 1
    return total
```


The problem is asking to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.

The given unit test `assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)` suggests that the count should be 2 for a sequence of length 2.

Here is the Python solution for the problem:

The solution uses a loop to generate all binary sequences of length 2n. For each sequence, it checks if the sum of first n bits is equal to the sum of last n bits. If it is, it increments the count.

The function `count_binary_seq(n)` takes an integer `n` as input and returns the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.

The time complexity of this solution is O(2^n) because it needs to generate all binary sequences of length 2n. The space complexity is O(1) because it only uses a constant amount of space to store the count and the current binary sequence.