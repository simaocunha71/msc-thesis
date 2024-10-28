In order to create a function that sums numbers from 1 to n, you can follow these steps:

1. Define a function called sum_to_n that takes an integer as input.
2. Initialize a variable called total to 0. This variable will store the sum of all the numbers.
3. Use a for loop to iterate through the range from 1 to n (inclusive). In each iteration, add the current number to the total.
4. After the loop is finished, return the total.

Here's an example implementation of the sum_to_n function in Python:

```python
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n."""
    total = 0
    for i in range(1, n+1):
        total += i
    return total
```

You can then test the function with different inputs to verify its correctness:

```python
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

In the provided implementation, the range function is used to generate a sequence of numbers from 1 to n (inclusive). The for loop iterates through this range, and in each iteration, the current number is added to the total using the += operator. Finally, the function returns the calculated total.

This implementation correctly computes the sum of numbers from 1 to n, as confirmed by the test cases.





































































































```