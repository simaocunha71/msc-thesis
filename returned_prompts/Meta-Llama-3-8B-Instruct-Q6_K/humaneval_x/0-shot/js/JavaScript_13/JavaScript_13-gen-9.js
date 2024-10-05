```python
def greatestCommonDivisor(a, b):
    if b == 0:
        return a
    else:
        return greatestCommonDivisor(b, a % b)
```
This function uses the Euclidean algorithm to find the greatest common divisor of two integers. It works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is 0. At that point, `a` is the greatest common divisor of the original `a` and `b`. 

For example, to find the greatest common divisor of 3 and 5, the function would work as follows:

* `a` = 3, `b` = 5: `a` is not 0, so replace `a` with `b` and `b` with the remainder of `a` divided by `b`. So `a` = 5, `b` = 3.
* `a` = 5, `b` = 3: `a` is not 0, so replace `a` with `b` and `b` with the remainder of `a` divided by `b`. So `a` = 3, `b` = 2.
* `a` = 3, `b` = 2: `a` is not 0, so replace `a` with `b` and `b` with the remainder of `a` divided by `b`. So `a` = 2, `b` = 1.
* `a` = 2, `b` = 1: `a` is not 0, so replace `a` with `b` and `b` with the remainder of `a` divided by `b`. So `a` = 1, `b` = 0.
* `a` = 1, `b` = 0: `b` is 0, so return `a`, which is 1.

Therefore, the greatest common divisor of 3 and 5 is 1. 

Similarly, to find the greatest common divisor of 25 and 15, the function would work as follows:

* `a` = 25, `b` = 15: `a` is not 0, so replace `a` with `b` and `b` with the remainder of `a` divided by `b`. So `