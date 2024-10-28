The problem asks to create a function that finds the closest smaller number to a given number n. 

However, the problem statement is not entirely clear. It does not specify whether the closest smaller number should be to the left or to the right of the given number. 

Fortunately, the unit test `assert closest_num(11) == 10` clarifies the problem. It implies that the function should return the closest smaller number to the left of the given number.

Here is a Python function that solves the problem:

```
def closest_num(n):
    for i in range(n-1, -1, -1):
        if i < n:
            return i
```

This function starts from n-1 and moves towards 0, checking each number to see if it's smaller than n. As soon as it finds a number that's smaller than n, it returns that number. This ensures that the function returns the closest smaller number to the left of the given number. 