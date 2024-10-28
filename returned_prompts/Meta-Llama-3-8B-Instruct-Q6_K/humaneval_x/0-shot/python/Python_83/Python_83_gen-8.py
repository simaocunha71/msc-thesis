
Explanation:
The given problem asks us to find the count of n-digit positive integers that start or end with 1.

Here is the Python code:

```Python
def starts_one_ends(n):
    if n == 1:
        return 10
    else:
        return (9 * (10 ** (n - 1))) + (9 * (10 ** (n - 1))) + 10
```

Explanation:
- The base case is when n is 1. In this case, we have 10 one-digit numbers that start or end with 1 (0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001).
- For n > 1, we have two cases:
  - Numbers that start with 1: We have 9 choices for the first digit (1 to 9), and then 10 choices for the remaining digits (since the number can end with any digit). So, we have 9 * (10 ** (n - 1)) such numbers.
  - Numbers that end with 1: We have 9 choices for the first (n - 1) digits, and then 1 choice for the last digit (1). So, we have 9 * (10 ** (n - 1)) such numbers.
  - We add these two cases together to get the total count.

For example, for n = 2, we have 90 numbers that start with 1 and end with any digit (19, 21, ..., 199), and 9 numbers that end with 1 and start with any digit (91, 101, ..., 991). So, the total count is 90 + 9 = 99.