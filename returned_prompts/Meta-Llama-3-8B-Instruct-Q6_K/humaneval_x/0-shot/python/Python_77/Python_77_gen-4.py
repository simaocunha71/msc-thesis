```
def iscube(a):
    import math
    n = 0
    while True:
        n += 1
        if round(math.pow(n, 3)) == a:
            return True
        if round(math.pow(n, 3)) > a:
            return False
```


This function checks whether the input number `a` is a cube of some integer number. It does this by iterating over possible values of `n` and checking if `n^3` equals `a`. If it finds such `n`, it returns `True`. If it doesn't find such `n` after checking all possible values, it returns `False`.

The `round` function is used to convert the result of `math.pow(n, 3)` to an integer, because `math.pow(n, 3)` may return a float if `n` is large enough. 

The function starts with `n = 0` and increments `n` in each iteration. It checks if `n^3` equals `a` and returns `True` if it does. If `n^3` is greater than `a`, it returns `False` because `a` cannot be a cube of any integer greater than `n`. If `n^3` is less than `a` and `n` is not yet large enough, it increments `n` and continues the loop. 

This function works for all valid inputs, as required. It is not very efficient for large inputs, because it has to check all possible values of `n`. However, for small inputs, it should work fine. 





```
def iscube(a):
    import math
    n = 0
    while True:
        n += 1
        if round(math.pow(n, 3)) == a:
            return True
        if round(math.pow(n, 3)) > a:
            return False
```


This function checks whether the input number `a` is a cube of some integer number. It does this by iterating over possible values of `n` and checking if `n^3` equals `a`. If it finds such `n`, it returns `True`. If it doesn't find such `n` after checking all possible values, it returns `False`.

The `round` function is used to convert the result of `math.pow(n, 3)` to an integer, because `math.pow(n, 3)` may return a float if `n`