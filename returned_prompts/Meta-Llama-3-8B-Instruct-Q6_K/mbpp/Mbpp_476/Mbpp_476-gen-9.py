```
def big_sum(arr):
    return sum(sorted(arr)[:1]) + sum(sorted(arr)[-1:])
```


Explanation: 
The function takes an array as input and returns the sum of the largest and smallest value in the array. 

We use the built-in `sorted` function to sort the array in ascending order. 

The `[:1]` syntax is used to get the first element (smallest value) and `[-1:]` is used to get the last element (largest value) of the sorted array. 

Finally, we use the `sum` function to calculate the sum of these two values.

The unit test `assert big_sum([1,2,3]) == 4` checks if the function works correctly for the input `[1,2,3]`. The expected output is `4` which is the sum of the smallest value `1` and the largest value `3`. 