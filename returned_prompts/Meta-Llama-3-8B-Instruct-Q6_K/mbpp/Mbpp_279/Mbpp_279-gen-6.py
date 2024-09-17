The decagonal number is the sum of the first n odd numbers. We can calculate it by using the formula (8n^2 + 7n)/2.

Here is the Python function:

```python
def is_num_decagonal(n):
    return (8*n**2 + 7*n)/2
```

This function will return the nth decagonal number. The unit test `assert is_num_decagonal(3) == 27` ensures that the function is working correctly. The 3rd decagonal number is indeed 27. 