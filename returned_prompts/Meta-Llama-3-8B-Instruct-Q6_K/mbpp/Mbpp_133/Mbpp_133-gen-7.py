```
def sum_negativenum(lst):
    return sum(num for num in lst if num < 0)
```
This function uses a generator expression to iterate over the list and sum up the negative numbers. The condition `num < 0` filters out the non-negative numbers. The `sum` function then adds up all the negative numbers. The unit test `assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32` ensures that the function works correctly. 