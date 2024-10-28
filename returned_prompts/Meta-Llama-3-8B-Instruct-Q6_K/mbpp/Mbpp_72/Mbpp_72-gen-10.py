```
def dif_Square(n):
    i = 0
    while (i * i) <= n:
        j = i
        while (j * j) <= n:
            if (i * i) - (j * j) == n:
                return True
            j += 1
        i += 1
    return False
```


The function `dif_Square(n)` checks whether the given number `n` can be represented as the difference of two squares or not. It uses two nested while loops to iterate over all possible values of `i` and `j` that can satisfy the condition `(i * i) - (j * j) == n`. If it finds such a pair, it returns `True`. If it doesn't find any such pair after checking all possible values of `i` and `j`, it returns `False`.

The unit test `assert dif_Square(5) == True` ensures that the function works correctly for the case where `n` is 5, which can be represented as the difference of two squares (25 - 16 = 9). The function should return `True` for this case. If the function doesn't work correctly, the test will fail.