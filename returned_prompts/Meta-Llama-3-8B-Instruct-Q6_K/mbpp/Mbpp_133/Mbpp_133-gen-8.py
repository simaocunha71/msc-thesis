```
def sum_negativenum(lst):
    return sum(i for i in lst if i < 0)
```



The task is to write a function that calculates the sum of all negative numbers in a given list of numbers. 

The provided unit test `assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32` suggests that the function should return the sum of all negative numbers in the list.

Here's a Python function that accomplishes this task:
```
def sum_negativenum(lst):
    return sum(i for i in lst if i < 0)
```
This function uses a generator expression to iterate over the list, and the `sum` function to calculate the sum of the negative numbers. The `if i < 0` condition filters out the non-negative numbers. The function returns the sum of the negative numbers. 





This function works as follows:
1. It iterates over each element `i` in the input list `lst`.
2. For each element `i`, it checks if `i` is less than 0 (i.e., if `i` is negative).
3. If `i` is negative, it includes `i` in the sum.
4. The `sum` function then adds up all the negative numbers and returns the result.

For example, if the input list is `[2, 4, -6, -9, 11, -12, 14, -5, 17]`, the function will return `-32`, which is the sum of the negative numbers in the list.