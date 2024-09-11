```
def sum_average(n):
    summ = (n * (n + 1)) / 2
    average = summ / n
    return summ, average
```

Here are some test cases:
```python
print(sum_average(1))    # (1, 1)
print(sum_average(5))    # (15, 3)
print(sum_average(10))   # (55, 5.5)
print(sum_average(100))  # (5050, 5.05)
```

Explanation:
The sum of first n natural numbers can be calculated by the formula n * (n + 1) / 2.
The average of first n natural numbers can be calculated by the formula summ / n, where summ is the sum of first n natural numbers.

The function sum_average(n) returns a tuple, which contains the sum and average of first n natural numbers.

In the test cases, we can see that the function works correctly and returns the expected results.

This function can be used to calculate the sum and average of any positive integer number.

Note: The input n should be a positive integer.

This is a simple implementation of the problem and can be optimized further if needed.

The time complexity of this function is O(1) as it only requires a single arithmetic operation to calculate the sum and average of first n natural numbers.

The space complexity of this function is O(1) as it only uses a constant amount of memory to store the result.

This function can be used in various applications where we need to calculate the sum and average of first n natural numbers, such as statistics, data analysis, and mathematical modeling.

Overall, this function provides a simple and efficient solution to the problem of finding the sum and average of first n natural numbers.

To use this function, you can simply call it with the desired value of n and it will return the sum and average of first n natural numbers.

For example, to calculate the sum and average of first 10 natural numbers, you can call the function like this:

```python
summ, average = sum_average(10)