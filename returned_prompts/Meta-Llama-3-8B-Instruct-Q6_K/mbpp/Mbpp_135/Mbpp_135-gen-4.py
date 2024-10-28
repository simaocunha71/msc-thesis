The nth hexagonal number is calculated by the formula n*(2n-1). The function should take an integer n as input and return the nth hexagonal number.

Here is the Python solution:
```
def hexagonal_num(n):
    return n*(2*n-1)
```
This function uses the formula n*(2n-1) to calculate the nth hexagonal number. For example, `hexagonal_num(10)` returns `190`, which is the 10th hexagonal number. The unit test `assert hexagonal_num(10) == 190` ensures that the function works correctly.