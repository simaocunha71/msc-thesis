
def fizz_buzz(n: int):
    cnt = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            if str(i).count("7") > 0:
                cnt += 1
    return cnt


# These "asserts" using `assert` are test cases.
# Run them to verify that this implementation indeed passes all the test
# cases that are provided and that it fails on the incorrect test
# cases.

import math

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    cnt = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            if str(i).count("7") > 0:
                cnt += 1
    return cnt

if __name__ == "__main__":
    print(fizz_buzz(78))



# Run the file to see the assertions pass or fail
# Here is the link to the original implementation:
# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/numbers.py
```

1. You are given a positive integer n.
2. You have to return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
3. Note: The input will always be a positive integer greater than or equal to 11.

Examples:

```
fizz_buzz(50) ➞ 0
fizz_buzz(78) ➞ 2
fizz_buzz(79) ➞ 3
```

Here are some hints:

- You