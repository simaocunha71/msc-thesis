
Here is the Python code that solves the problem:

```
def starts_one_ends(n):
    count = 0
    for i in range(10**(n-1), 10**n):
        if str(i)[0] == '1' or str(i)[-1] == '1':
            count += 1
    return count
```

Explanation:
The function starts_one_ends takes an integer n as input and returns the count of n-digit positive integers that start or end with 1.

Here's how it works:

1. Initialize a counter variable count to 0.
2. Iterate over the range of numbers from 10^(n-1) to 10^n. This range includes all n-digit positive integers.
3. For each number i in the range, convert it to a string using the str() function.
4. Check if the first character (0-indexed) of the string is '1' or the last character of the string is '1'. If either condition is true, increment the count variable.
5. After iterating over all numbers in the range, return the count variable, which represents the number of n-digit positive integers that start or end with 1.

For example, if you call starts_one_ends(2), the function will return 11, because there are 11 two-digit positive integers that start or end with 1 (10, 11, 12, ..., 19, 21, 31, ..., 91, 101). If you call starts_one_ends(3), the function will return 21, because there are 21 three-digit positive integers that start or end with 1 (100, 101, 102, ..., 199, 201, 301, ..., 901, 1001). And so on.