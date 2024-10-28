The nth tetrahedral number is given by the formula (n*(n+1)*(n+2))/6. Here is the Python function that calculates it:

```python
def tetrahedral_number(n):
    return (n*(n+1)*(n+2))/6
```

This function takes an integer `n` as input and returns the `n`th tetrahedral number. For example, `tetrahedral_number(5)` returns `35`. The unit test `assert tetrahedral_number(5) == 35` ensures that the function is working correctly. 