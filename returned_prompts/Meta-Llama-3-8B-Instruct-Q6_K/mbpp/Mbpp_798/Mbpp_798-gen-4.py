```
def _sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
```


This function takes an array as input, initializes a variable `total` to 0, then iterates over each number in the array, adding it to `total`. Finally, it returns the sum. The unit test `assert _sum([1, 2, 3]) == 6` ensures the function works correctly for the input `[1, 2, 3]`. 

Note: Python has a built-in function `sum()` that can be used to calculate the sum of an array. So, a more concise and efficient way to solve this problem would be:
```
def _sum(arr):
    return sum(arr)
```


However, the original problem statement asked to write a function to find the sum of an array, so I provided a solution that manually calculates the sum. If the goal is to use a built-in function, the above one-liner solution would be more suitable. 