The problem is asking for a function that calculates the nth tetrahedral number. The tetrahedral number is the sum of the first n positive integers. For example, the first few tetrahedral numbers are 1, 4, 10, 20, 35, ...

Here is the solution in Python:
```
def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 6
```
This function uses the formula for the nth tetrahedral number, which is n * (n + 1) * (n + 2) / 6. The `//` operator is used for integer division, which ensures that the result is an integer.

The unit test `assert tetrahedral_number(5) == 35` confirms that the function works correctly for n = 5. It checks if the result of the function is equal to 35, which is the correct value for the 5th tetrahedral number. If the function is correct, this test will pass, otherwise it will raise an AssertionError. 