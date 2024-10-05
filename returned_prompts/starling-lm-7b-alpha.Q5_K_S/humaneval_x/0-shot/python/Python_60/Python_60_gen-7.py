To solve this problem, you can define a function called sum_to_n that takes an integer n as a parameter. Inside the function, you can use the formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to n. The formula is given by the equation: sum = (n * (n + 1)) / 2. Finally, you can return the calculated sum. Here's an example of how you can implement this solution in Python:

```python
def sum_to_n(n: int):
    sum = (n * (n + 1)) // 2
    return sum
```

To test the function, you can use the provided doctest comments to verify that the function returns the correct results for different values of n.

```python
def sum_to_n(n: int):
    sum = (n * (n + 1)) // 2
    return sum
```

Here are some test cases you can use to verify the correctness of the function:

```python
# Test cases
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

By running these test cases, you can ensure that the sum_to_n function is working correctly and producing the expected results.

```python
# Test cases
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

By running these test cases, you can ensure that the sum_to_n function is working correctly and producing the expected results.

```python
# Test cases
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to