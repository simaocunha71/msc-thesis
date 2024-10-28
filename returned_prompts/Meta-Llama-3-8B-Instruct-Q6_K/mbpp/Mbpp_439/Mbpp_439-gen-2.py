You can use the following function to join a list of multiple integers into a single integer:

```python
def multiple_to_single(lst):
    result = 0
    for num in lst:
        result = result * 10 + num
    return result
```

This function works by iterating over the list of integers and appending each integer to the result, shifting the digits to the left by multiplying the result by 10. The function will return the joined integer. For example, if the input list is [11, 33, 50], the function will return 113350. This is confirmed by the unit test `assert multiple_to_single([11, 33, 50])==113350`. 