```
def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
    return min_diff
```
The function `find_min_diff` takes two parameters: an array of numbers and the length of the array. It first sorts the array in ascending order. Then it iterates over the array, starting from the second element (index 1). For each element, it calculates the difference with the previous element and updates the `min_diff` if the new difference is smaller. Finally, it returns the minimum difference found.

The unit test `assert find_min_diff((1,5,3,19,18,25),6) == 1` ensures that the function works correctly. It checks that the minimum difference between any two elements in the array `(1,5,3,19,18,25)` is `1`. This is because the elements `3` and `5` have a difference of `1`, which is the smallest difference in the array. 

Note: The function assumes that the input array has at least two elements. If the array has only one element, the function will return `float('inf')`, which is a reasonable default value for the minimum difference. If you want to handle the case of an array with only one element differently, you can add a special case at the beginning of the function. 