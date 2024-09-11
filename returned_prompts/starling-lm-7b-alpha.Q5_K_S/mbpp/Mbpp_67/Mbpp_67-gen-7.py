Here's one way you can do it:

```python
def bell_number(n):
    # Create an array of size n+1 to store the Bell numbers
    bells = [0] * (n + 1)
    # Set the base case: the Bell number of 0 is 1
    bells[0] = 1
    # Use dynamic programming to calculate the remaining Bell numbers
    for i in range(1, n + 1):
        # For each number, the Bell number is the sum of all the partitions of the previous numbers
        for j in range(i):
            bells[i] += bells[j] * bells[i - j - 1]
    # Return the Bell number of n
    return bells[n]
```

This function uses dynamic programming to calculate the Bell numbers in a top-down manner. It initializes an array `bells` of size `n + 1` to store the Bell numbers. The base case is that the Bell number of 0 is 1, so we set `bells[0] = 1`. Then, for each number from 1 to `n`, we calculate the Bell number by summing up all the partitions of the previous numbers. This is done using a nested loop, where the outer loop iterates over the numbers from 0 to `i`, and the inner loop iterates over the numbers from 0 to `i - j - 1`. Finally, we return the Bell number of `n`.

To test the function, you can use the `assert` statement to check if the function correctly calculates the Bell number for a given input. For example, `assert bell_number(2)==2` checks if the Bell number of 2 is equal to 2, which should be `True`.

```python
def bell_number(n):
    # Create an array of size n+1 to store the Bell numbers
    bells = [0] * (n + 1)
    # Set the base case: the Bell number of 0 is 1
    bells[0] = 1
    # Use dynamic programming to calculate the remaining Bell numbers
    for i in range(1, n + 1):
        # For each number, the Bell number is the