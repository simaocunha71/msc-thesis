```
def big_sum(arr):
    return max(arr) + min(arr)
```



The problem is asking to write a function that takes an array as input and returns the sum of the largest and smallest values in the array. 

The given unit test `assert big_sum([1,2,3]) == 4` suggests that the function should return the sum of the smallest and largest values in the array. 

The Python function `big_sum` can be written as follows: 

```
def big_sum(arr):
    return max(arr) + min(arr)
```

This function uses the built-in `max` and `min` functions in Python to find the largest and smallest values in the array, and then returns their sum. 

For example, if the input array is `[1,2,3]`, the function will return `1 + 3 = 4`, which passes the given unit test. 