The nth hexagonal number can be calculated by the formula: Hn = n(2n - 1). Here is the Python function that calculates the nth hexagonal number:

```Python
def hexagonal_num(n):
    return n * (2 * n - 1)
```
This function takes an integer n as input and returns the nth hexagonal number. The unit test `assert hexagonal_num(10) == 190` ensures that the function is working correctly. For example, `hexagonal_num(10)` should return `190`, which is the 10th hexagonal number. 