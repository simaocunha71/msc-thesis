The nth hexagonal number can be calculated by the formula: Hn = n*(2n-1).
Here is the Python function that implements this formula:

```python
def hexagonal_num(n):
    return n * (2 * n - 1)
```

This function takes an integer n as input and returns the nth hexagonal number. For example, hexagonal_num(10) returns 190, which is the 10th hexagonal number. The unit test `assert hexagonal_num(10) == 190` ensures that the function is working correctly. 

This function has a time complexity of O(1), which means it runs in constant time, and a space complexity of O(1), which means it uses a constant amount of space. Therefore, it is efficient and can handle large inputs. 