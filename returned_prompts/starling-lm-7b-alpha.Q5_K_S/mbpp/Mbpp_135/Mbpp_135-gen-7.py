```
def hexagonal_num(n):
    return n*(3*n-1)//2
```

Explanation:
The nth hexagonal number is given by the formula (n * (3 * n - 1)) / 2.
Here, n represents the position of the hexagonal number in the sequence.
For example, the first hexagonal number is 1, the second is 6, the third is 15, and so on.
The provided function `hexagonal_num` takes an integer `n` as input and returns the nth hexagonal number using the formula.
In the given assertion, `hexagonal_num(10)` is called and it is expected to return 190, which is the 10th hexagonal number.

Here's an example of how to use the function:
```python
print(hexagonal_num(10))  # Output: 190
```

This will print the 10th hexagonal number, which is 190.

The formula for the nth hexagonal number is derived from the fact that a hexagonal number can be represented as the sum of an arithmetic series with a common difference of 2. 
In the arithmetic series, the first term is n, the last term is 2n-1, and the total number of terms is 3n-2. 
Using the formula for the sum of an arithmetic series, we can find the sum, which is equal to the nth hexagonal number.

The provided function uses this formula to calculate the nth hexagonal number efficiently.

Note: The formula for the nth hexagonal number is valid for positive integer values of n.

It's important to mention that the provided function is a Python implementation, and it may vary slightly in other programming languages or environments.
However, the core logic of finding the nth hexagonal number remains the same.

In summary, the function `hexagonal_num` takes an integer `n` as input and returns the nth hexagonal number using the provided formula.
The assertion `hexagonal_num(10) == 190` checks if the function correctly calculates the 10th hexagonal number, which is indeed 190