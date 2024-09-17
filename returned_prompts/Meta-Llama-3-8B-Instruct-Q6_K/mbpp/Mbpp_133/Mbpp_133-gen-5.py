```
def sum_negativenum(lst):
    return sum(num for num in lst if num < 0)
```
This function uses a generator expression to iterate over the input list and sum up the negative numbers. The built-in `sum` function is used to calculate the sum. The condition `num < 0` filters out the non-negative numbers. 

The unit test `assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32` ensures that the function works correctly. 

This solution has a time complexity of O(n), where n is the number of elements in the input list, because it needs to iterate over the entire list. The space complexity is O(1), because it uses a constant amount of space to store the sum and the generator expression. 