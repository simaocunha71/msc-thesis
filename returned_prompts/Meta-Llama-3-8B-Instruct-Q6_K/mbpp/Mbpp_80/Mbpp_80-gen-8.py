The tetrahedral numbers are a sequence of numbers that can be represented by the formula 1 + 3 + 6 + ... + n*(n+1)/2. This formula represents the sum of the first n triangular numbers.

Here is a Python function to find the nth tetrahedral number:
```
def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 6
```
This function uses the formula to calculate the nth tetrahedral number. The `//` operator is used for integer division, which ensures that the result is an integer.

The function can be tested with the unit test `assert tetrahedral_number(5) == 35`, which checks that the 5th tetrahedral number is indeed 35.