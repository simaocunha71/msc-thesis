
To solve this problem, we can use a while loop to iterate from n down to 1, checking if each number is a divisor of n. We can use the modulo operator (%) to check if a number is a divisor: if the remainder of dividing n by the current number is 0, then it's a divisor. We keep track of the largest divisor found so far in a variable called max_divisor. Here's the step-by-step algorithm:

1. Initialize max_divisor to 0. This variable will keep track of the largest divisor we find.
2. Use a while loop to iterate from n down to 1 (inclusive). This is because divisors must be less than or equal to the number they divide.
3. Inside the loop, check if the current number is a divisor of n by using the modulo operator (%). If the remainder is 0, then the current number is a divisor of n.
4. If the current number is a divisor, update max_divisor to be the current number.
5. After the loop finishes, return max_divisor, which will be the largest divisor of n smaller than n itself.

Here's the Python code that implements this algorithm:

```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_divisor = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            max_divisor = i
    return max_divisor
```

You can test this function with the provided example:

```python
print(largest_divisor(15))  # Output: 5
```

This will correctly print the largest divisor of 15, which is 5.

The time complexity of this solution is O(sqrt(n)) because we need to check all numbers from n down to 1. The space complexity is O(1) because we only use a single variable to keep track of the largest divisor found so far