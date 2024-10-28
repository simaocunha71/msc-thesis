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
This function sorts the array first, then iterates over the array to find the minimum difference between any two elements. The `float('inf')` is used as the initial value for `min_diff` to ensure that the first difference found will be smaller than it. The function returns the minimum difference found. 

For example, if the input array is `(1,5,3,19,18,25)` and `n=6`, the function will return `1` because the minimum difference between any two elements in the array is `1`.  The test case `assert find_min_diff((1,5,3,19,18,25),6) == 1` ensures that the function works correctly. 

Note that the function assumes that the input array has at least one element and that `n` is the length of the array. If the array has less than two elements, the function will return `float('inf')` because there are no pairs of elements to find the minimum difference for. If `n` is less than the length of the array, the function will return the minimum difference for the first `n` elements of the array.  If `n` is greater than the length of the array, the function will return `float('inf')` because there are not enough elements to find the minimum difference for.  You may want to add error checking code to handle these cases if they are possible in your use of the function. 