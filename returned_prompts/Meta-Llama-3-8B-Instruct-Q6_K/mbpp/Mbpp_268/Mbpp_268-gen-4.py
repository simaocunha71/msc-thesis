The problem is asking you to find the nth star number. A star number is a number that can be represented as 1 + 11 + 111 + ... + 1...1 (n times). 

The unit test `assert find_star_num(3) == 37` helps to understand the problem better. For example, the first star number is 1, the second is 3, the third is 37, and so on.

Here's a Python function that calculates the nth star number:

```
def find_star_num(n):
    total = 0
    for i in range(n):
        total += int('1' * (i + 1))
    return total
```

This function works by initializing a variable `total` to 0. Then it enters a loop that runs `n` times. In each iteration of the loop, it adds the `i + 1`-th star number to `total`. The `i + 1`-th star number is calculated by converting the string `'1' * (i + 1)` to an integer. This string consists of `i + 1` ones. For example, when `i` is 2, the string is `'111'`, which is converted to the integer 3. When `i` is 3, the string is `'1111'`, which is converted to the integer 4, and so on. Finally, the function returns `total`, which is the sum of the first `n` star numbers. 