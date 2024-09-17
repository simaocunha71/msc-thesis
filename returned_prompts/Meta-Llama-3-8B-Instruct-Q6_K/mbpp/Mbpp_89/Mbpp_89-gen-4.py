```
def closest_num(n):
    if n <= 0:
        return None
    for i in range(n-1, 0, -1):
        if i < n:
            return i
```


Explanation:
The problem asks to write a function that finds the closest smaller number than a given number `n`. For example, if `n` is 11, the closest smaller number is 10.

The function iterates from `n-1` to 1 (inclusive) in reverse order. It returns the first number `i` that is less than `n`. If `n` is 0 or negative, the function returns `None`.

The unit test `assert closest_num(11) == 10` helps to clarify the problem by providing an example of the expected output. In this case, the expected output is 10, which is the closest smaller number to 11.