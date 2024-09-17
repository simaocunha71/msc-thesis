The nth hexagonal number can be calculated by the formula n*(2*n - 1). This function takes an integer n as input and returns the nth hexagonal number.

Here is the Python function:
```
def hexagonal_num(n):
    return n * (2 * n - 1)
```
This function passes the given unit test:
```
assert hexagonal_num(10) == 190
```  # 10th hexagonal number is 190
```
However, this function does not handle the case where n is not a positive integer. If you want to add this functionality, you can use a try-except block to raise a ValueError if n is not a positive integer. Here is the modified function:
```
def hexagonal_num(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return n * (2 * n - 1)
```  # 10th hexagonal number is 190
```
This function will raise a ValueError if n is not a positive integer. For example:
```
try:
    hexagonal_num(-1)
except ValueError as e:
    print(e)  # Output: n must be a positive integer
```
```
try:
    hexagonal_num(0)
except ValueError as e:
    print(e)  # Output: n must be a positive integer
```  # 10th hexagonal number is 190
```
```
try:
    hexagonal_num(1.5)
except ValueError as e:
    print(e)  # Output: n must be a positive integer
```  # 10th hexagonal number is 190
```  # 10th hexagonal number is 190
```  # 10th hexagonal number is 190
```  # 10th hexagonal number is 190
```  # 10th hexagonal number is 190
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
