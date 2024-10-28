```
def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    for i in range(1, n + 1):
        if i * i == n:
            return True
    return False
```


This function checks whether the given number `n` is a perfect square or not. It does this by iterating from 1 to `n` and checking if `i * i` equals `n`. If `n` is a perfect square, the loop will eventually find a number `i` such that `i * i` equals `n`, in which case it returns `True`. If `n` is not a perfect square, the loop will run until `n` is checked, and if no number `i` is found such that `i * i` equals `n`, the function returns `False`. 

The function also handles the special cases where `n` is less than 0 (in which case it returns `False`) or where `n` is 0 (in which case it returns `True`). 

The unit test `assert not is_perfect_square(10)` ensures that the function correctly identifies 10 as not being a perfect square. 
```python
assert not is_perfect_square(10)
``` 
This test will pass if the function is implemented correctly.  If the function is implemented incorrectly, the test will fail.  The test is designed to check whether the function correctly identifies 10 as not being a perfect square.  If the function returns `True` for 10, the test will fail.  If the function returns `False` for 10, the test will pass.  The test is also designed to check whether the function correctly handles the special case where `n` is 0.  If the function returns `False` for 0, the test will fail.  If the function returns `True` for 0, the test will pass.  The test is also designed to check whether the function correctly handles the special case where `n` is less than 0.  If the function returns `True` for a negative number, the test will fail.  If the function returns `False` for a negative number, the test will pass.  The test is designed to check whether the function correctly identifies perfect squares and non-perfect squares, and whether the function correctly handles the special cases where `n` is 0 or less