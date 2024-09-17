```
def big_sum(arr):
    return max(arr) + min(arr)
```
This function takes an array as input and returns the sum of the largest and smallest values in the array. The `max` function is used to find the largest value and the `min` function is used to find the smallest value. The sum of these two values is then returned. The unit test `assert big_sum([1,2,3]) == 4` ensures that the function works correctly by checking that the sum of the largest and smallest values in the array `[1,2,3]` is indeed `4`.